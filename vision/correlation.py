import sys
from keras.models import load_model
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns
from scipy.cluster import hierarchy
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle

from lib.attlayer import AttentionWeightedAverage


MODEL_PATH = '/home/daniel/heMoji/logs/model_3G_generatorBatch.hdf5'
DATA_PATH = '/home/daniel/heMoji/data/data_3G.pkl'
VOCAB_PATH = '/home/daniel/heMoji/data/vocab_3G.json'
OUTPUT_PATH = '/home/daniel/heMoji/logs/'
DATA_TYPE = "deep"


class Correlation():
    """
    makes 2 graphs based on the 2 vectors (y_gold and y_pred):
    1. confusion matrix
    2. hierarchy graph
    """
    def __init__(self, y_gold, y_pred, l2e, output_path, name_prefix=None, save=True):
        # make y_gold vec into 1-dim vec
        self.y_gold = y_gold
        if len(self.y_gold.shape) > 1:
            self.y_gold = self.y_gold.argmax(axis=1)
        # make y_pred vec into 1-dim vec
        self.y_pred = y_pred
        if len(self.y_pred.shape) > 1:
            self.y_pred = self.y_pred.argmax(axis=1)
        self.l2e = l2e
        self.output_path = output_path
        if name_prefix is not None:
            self.name_prefix = name_prefix + "_"
        else:
            self.name_prefix = ""
        self.save = save

        # build confusion matrix
        print("Making confusion matrix & hierarchy graph for {0} data ...".format(self.name_prefix))
        matrix = confusion_matrix(self.y_gold, self.y_pred, labels=np.asarray(self.l2e.keys()))
        self.df = pd.DataFrame(matrix)

    def make_graphs(self):
        self._make_confusion_graph()
        self._make_hierachy_graph()

    def _make_confusion_graph(self):
        plt.figure(figsize=(20, 14))
        dashboard = sns.heatmap(self.df, annot=False, cmap=sns.cubehelix_palette(n_colors=100))

        labels_str_list = [str(i) for i in list(self.l2e.keys())]
        labels = np.arange(len(self.l2e))

        dashboard.set_xticks(labels)
        dashboard.set_xticklabels(labels_str_list, fontsize=7, minor=False)
        dashboard.xaxis.set_ticks_position('top')

        dashboard.set_yticks(labels)
        dashboard.set_yticklabels(labels_str_list, fontsize=7, minor=False, rotation=0)

        # emojis_ticks = [(str(i) + '\n' + l2e[i]) for i in range(len(l2e))]
        # ax = plt.axes()
        # ax.set_xticklabels(emojis_ticks)
        # ax.set_yticklabels(emojis_ticks)

        plt.suptitle('Correlation Matrix of Predictions', fontsize=20)
        plt.ylabel('True label', fontsize=12)
        plt.xlabel('Predicted label', fontsize=12)
        # show x axis label at top
        dashboard.xaxis.set_label_position('top')
        # show ticks both bottom and top
        plt.tick_params(axis='both', which='major',  labelbottom=True, bottom=True, top=True, labeltop=True)
        plt.grid()

        if self.save:
            path = self.output_path + "/{0}confusion_mat.pdf".format(self.name_prefix)
            plt.savefig(path, dpi=600, format='pdf')
        else:
            plt.show()

        plt.close()

    def _make_hierachy_graph(self):
        plt.figure(figsize=(20, 14))
        # build histogram
        # Y = hierarchy.distance.pdist(self.df.values, metric='euclidean')
        try:
            Z = hierarchy.linkage(self.df.corr(), method='ward', optimal_ordering=True)
        except ValueError as e:
            print("[WARNING] can not calculate corr of confusion matrix. That is bug if it is in production.")
            Z = hierarchy.linkage(self.df.values, method='ward', optimal_ordering=True)
        ax = hierarchy.dendrogram(Z, leaf_rotation=0, leaf_font_size=12, color_threshold=1.5)

        if self.save:
            path = self.output_path + "/{0}hierarchy_graph.pdf".format(self.name_prefix)
            plt.savefig(path, dpi=600, format='pdf')
        else:
            plt.show()

        plt.close()


def get_args():
    if len(sys.argv) == 6:
        model_path = sys.argv[1]
        data_path = sys.argv[2]
        vocab_path = sys.argv[3]
        output_path = sys.argv[4]
        data_type = sys.argv[5]
    else:
        model_path = MODEL_PATH
        data_path = DATA_PATH
        vocab_path = VOCAB_PATH
        output_path = OUTPUT_PATH
        data_type = DATA_TYPE

    e2l_str = DATA_TYPE + "e2l"
    l2e_str = "l2e" + DATA_TYPE
    exec "from src.emoji2label import %s as e2l" % e2l_str
    exec "from src.emoji2label import %s as l2e" % l2e_str

    return model_path, data_path, vocab_path, output_path, data_type, e2l, l2e


def get_model(model_path):
    model = load_model(model_path, custom_objects={'AttentionWeightedAverage': AttentionWeightedAverage})
    model.summary()

    return model


def load_vocab(vocab_path):
    with open(vocab_path, 'r') as f:
        vocab = json.load(f)
        print("Vocab size is: {0}".format(len(vocab)))

    return vocab


if __name__ == '__main__':
    """
    load model, predict test_set, build confusion matrix, and based on it - hierarchy diagram
    """
    # this should be here instead of the top fo the file to prevent importing loop
    # from src.train_model import loadData, splitData, padData
    model_path, data_path, vocab_path, output_path, data_type, e2l, l2e = get_args()
    # vocab = load_vocab(vocab_path)
    # model = get_model(model_path)
    # (X, Y) = loadData(data_path)
    # params = dict()
    # params["uint"] = 32
    # params["maxlen"] = 80
    # (x_train, x_dev, x_test), (y_train, y_dev, y_test) = splitData(X, Y, vocab, params, e2l)
    # (x_train, x_dev, x_test) = padData(x_train, x_dev, x_test, params)
    # print("Predicting ...")
    # y_pred_vec = model.predict(x_test)
    # y_pred = y_pred_vec.argmax(axis=1)

    with open('/home/daniel/heMoji/logs/y_pred.pkl', 'rb') as f:
        y_pred = pickle.load(f)
    with open('/home/daniel/heMoji/logs/y_gold.pkl', 'rb') as f:
        y_gold = pickle.load(f)

    c = Correlation(y_gold, y_pred, l2e, output_path, save=False)
    c.make_graphs()
