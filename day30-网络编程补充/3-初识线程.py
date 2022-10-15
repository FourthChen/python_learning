# -*- coding:utf-8 -*-
import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import cv2


# ����ǩת��Ϊ����������['123dad','1323ds'],���[[0,1,1.....0,0],[0,1,1....,0,0]]
def text2vec(labels):
    # �����ʵ�
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    dictionary = number + alphabet

    label_new = []
    # ��y��ǩת��Ϊone-hot����
    for label in labels:
        y_name = list(label)
        y_label = []
        for i in range(6):
            y_label.append(np.zeros(len(dictionary)))
        y_label = np.array(y_label)

        # ��ʼ����ɣ�ת��Ϊone-hot����
        for i in range(len(y_name)):
            if y_name[i] == '.':
                print(y_name)
                continue
         #   print(y_name)
            key = dictionary.index(y_name[i])
            y_label[i][key] = 1
        y_label = y_label.reshape(-1)
        label_new.append(y_label)
    return label_new


# ������ת��Ϊ��ǩ,����[[ 5 31  5  4  3  6],[2 4 5 5 3 3]�����['123dad','1323ds']
def vec2text(y_vectors):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    dictionary = number + alphabet
    y_names = []

    for y_vector in y_vectors:
        y_name_new = []
        for y_key in y_vector:
            y_name_new.append(dictionary[int(y_key)])
        y_name = ''.join(y_name_new)
        y_names.append(y_name)
    return y_names


def load_data(img_dir):
    # ��������
    data = []
    labels = []
    img_name = os.listdir(img_dir)

    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        # cv2��������ͼƬ��RGB3ά�ģ�ת�ɻҶ�ͼ����ͼƬת����1ά
        image = cv2.imread(path)
        data.append(image)
        y_temp = img_name[i][:6]
        labels.append(y_temp)

    label_new = text2vec(labels)
    # ��ǩ�淶��
    x = np.array(data)
    y = np.array(label_new)
    return x, y


def load_predict_data(img_dir):
    # ��������
    data = []
    img_name = os.listdir(img_dir)
    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        # cv2��������ͼƬ��RGB3ά�ģ�ת�ɻҶ�ͼ����ͼƬת����1ά
        image = cv2.imread(path)
        data.append(image)
    x = np.array(data)
    return x

def load_test_data(img_dir):
    # ��������
    data = []
    labels = []
    img_name = os.listdir(img_dir)

    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        # cv2��������ͼƬ��RGB3ά�ģ�ת�ɻҶ�ͼ����ͼƬת����1ά
        image = cv2.imread(path)
        data.append(image)
        y_temp = img_name[i][:6]
        labels.append(y_temp)
    # ��ǩ�淶��
    x = np.array(data)
    y = np.array(labels)
    return x, y


class Vgg16:
    vgg_mean = [103.939, 116.779, 123.68]

    def __init__(self, vgg16_npy_path=None, restore_from=None):
        # pre-trained parameters
        try:
            self.data_dict = np.load(vgg16_npy_path, encoding='latin1').item()
        except FileNotFoundError:
            print('Please download VGG16 parameters from here https://mega.nz/#!YU1FWJrA!O1ywiCS2IiOlUCtCpI6HTJOMrneN-Qdv3ywQP5poecM\nOr from my Baidu Cloud: https://pan.baidu.com/s/1Spps1Wy0bvrQHH2IMkRfpg')

        self.tfx = tf.placeholder(tf.float32, [None, 224, 224, 3])
        self.tfy = tf.placeholder(tf.float32, [None, 216])
        self.keep_prob = tf.placeholder(tf.float32)
        print('hello')
        # Convert RGB to BGR
        red, green, blue = tf.split(axis=3, num_or_size_splits=3, value=self.tfx * 255.0)
        bgr = tf.concat(axis=3, values=[
            blue - self.vgg_mean[0],
            green - self.vgg_mean[1],
            red - self.vgg_mean[2],
        ])

        # pre-trained VGG layers are fixed in fine-tune
        conv1_1 = self.conv_layer(bgr, "conv1_1")
        conv1_2 = self.conv_layer(conv1_1, "conv1_2")
        pool1 = self.max_pool(conv1_2, 'pool1')

        conv2_1 = self.conv_layer(pool1, "conv2_1")
        conv2_2 = self.conv_layer(conv2_1, "conv2_2")
        pool2 = self.max_pool(conv2_2, 'pool2')

        conv3_1 = self.conv_layer(pool2, "conv3_1")
        conv3_2 = self.conv_layer(conv3_1, "conv3_2")
        conv3_3 = self.conv_layer(conv3_2, "conv3_3")
        pool3 = self.max_pool(conv3_3, 'pool3')

        conv4_1 = self.conv_layer(pool3, "conv4_1")
        conv4_2 = self.conv_layer(conv4_1, "conv4_2")
        conv4_3 = self.conv_layer(conv4_2, "conv4_3")
        pool4 = self.max_pool(conv4_3, 'pool4')

        conv5_1 = self.conv_layer(pool4, "conv5_1")
        conv5_2 = self.conv_layer(conv5_1, "conv5_2")
        conv5_3 = self.conv_layer(conv5_2, "conv5_3")
        pool5 = self.max_pool(conv5_3, 'pool5')

        with tf.variable_scope("new_train"):
            self.flatten = tf.reshape(pool5, [-1, 7 * 7 * 512])
            self.fc6 = tf.layers.dense(self.flatten, 512, tf.nn.relu,
                                       kernel_regularizer=tf.contrib.layers.l2_regularizer(0.001),name='fc6')
           # self.fc6 = tf.layers.dense(self.flatten, 432, tf.nn.relu,name='fc6')
            self.out = tf.layers.dense(self.fc6, 216, name='out')

        # ����׼ȷ��
        self.y_pre = tf.reshape(self.out, [-1, 6, 36])
        self.y_predict_vec = tf.argmax(self.y_pre, 2)    # ����Ԥ�⣬ת���ɣ�6��36��
        y_label = tf.reshape(self.tfy, [-1, 6, 36])
        correct_pred = tf.equal(tf.argmax(self.y_pre, 2), tf.argmax(y_label, 2))
        self.accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
        # tf.summary.scalar('accuracy', self.accuracy)

        config = tf.ConfigProto(device_count={"CPU": 2},
                                inter_op_parallelism_threads=2,
                                intra_op_parallelism_threads=2,
                               log_device_placement=True)

        self.sess = tf.Session(config=config)

        if restore_from:
            saver = tf.train.Saver()
            saver.restore(self.sess, restore_from)
        else:   # training graph
            diff = tf.nn.sigmoid_cross_entropy_with_logits(logits=self.out, labels=self.tfy)
            self.loss = tf.reduce_mean(diff)
            # tf.summary.scalar('loss', self.loss)
            # ����㲻ѵ����ȫ���Ӳ����΢��
            output_layer_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope="new_train")
            # ʹ��AdamOptimizer�Ż���ѵ��ģ�ͣ���С����������ʧ
            optimizer = tf.train.AdamOptimizer(learning_rate=0.0001, name="Adam2")
            self.train_op = optimizer.minimize(self.loss, var_list=output_layer_vars)
            self.sess.run(tf.global_variables_initializer())

    def max_pool(self, bottom, name):
        return tf.nn.max_pool(bottom, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name=name)

    def conv_layer(self, bottom, name):
        with tf.variable_scope(name):   # CNN's filter is constant, NOT Variable that can be trained
            conv = tf.nn.conv2d(bottom, self.data_dict[name][0], [1, 1, 1, 1], padding='SAME')
            lout = tf.nn.relu(tf.nn.bias_add(conv, self.data_dict[name][1]))
            return lout

    def train(self, x, y,keep_prob):
        loss, __ = self.sess.run([self.loss, self.train_op], {self.tfx: x, self.tfy: y, self.keep_prob:keep_prob})
        return loss

    def predict(self, img_dir):
        x, y= load_test_data(img_dir)
        y_predict = self.sess.run([self.y_predict_vec], {self.tfx: x})
        return y_predict, y

    # Ԥ�ⵥ��ͼƬ
    def predict_sigle(self, img_dir):
        x = load_predict_data(img_dir)
        y_predict = self.sess.run([self.y_predict_vec], {self.tfx:x})
        return y_predict

    def save(self, path='./for_transfer_learning/models/transfer_learn',step=1):
        saver = tf.train.Saver()
        saver.save(self.sess, path, write_meta_graph=False,global_step=step)


def train():
    # load image data sets

    img_dir = './img_down_sets/new_corpus'

    x, y = load_data(img_dir)

    # ���ѵ���������������
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.016)
    #  training and then save the model
    vgg = Vgg16(vgg16_npy_path='./for_transfer_learning/vgg16.npy')
    print('Net built')
    for i in range(20000):
        b_idx = np.random.randint(0, len(x_train), 100)
        if (i+1) % 100 ==0:
            train_accuracy = vgg.sess.run([vgg.accuracy],{vgg.tfx:x_test[:100], vgg.tfy:y_test[:100],vgg.keep_prob:1.0})
            print('train accuracy:%s'% train_accuracy)
        train_loss= vgg.train(x_train[b_idx], y_train[b_idx], keep_prob=0.5)
        if (i+1) % 10 ==0:
            print(i+1, 'train loss: %s'% (train_loss))
        if (i+1) % 200 == 0:
            test_accuracy = vgg.sess.run([vgg.accuracy], {vgg.tfx: x_test[:100], vgg.tfy: y_test[:100],vgg.keep_prob:1.0})
            print("**********test accuracy:%s" % test_accuracy)
            test_accuracy = vgg.sess.run([vgg.accuracy], {vgg.tfx: x_test[100:200], vgg.tfy: y_test[100:200],vgg.keep_prob:1.0})
            print("**********test accuracy:%s" % test_accuracy)
        if (i+1) % 200 == 0 and test_accuracy[0] > 0.7:
            vgg.save('./for_transfer_learning/models/transfer_learn',i)      # save learned fc layers
    # compute the test image accuracy


def evalate():
    vgg = Vgg16(vgg16_npy_path='./for_transfer_learning/vgg16.npy',
                restore_from='./for_transfer_learning/models/transfer_learn-799')
    img_dir = './img_down_sets/img_test_border'
    y_predict, y = vgg.predict(img_dir)
    y_predict = np.array(y_predict)
    # print(y_predict[0])
    # print(y)
    y_name = vec2text(y_predict[0])
    count = 0
    for i in range(len(y_name)):
        if y[i] == y_name[i]:
            count+=1
        print("��ǩ��%s�� Ԥ�⣺%s,  %s" % (y[i], y_name[i], y[i] == y_name[i]))
    accuracy = (count/len(y_name))*100
    print("accuracy:%s%%"% accuracy)

def predict():
    vgg = Vgg16(vgg16_npy_path='./for_transfer_learning/vgg16.npy',
                restore_from='./for_transfer_learning/models/transfer_learn-999')
    img_dir = './img_down_sets/test'
    y_predict = vgg.predict_sigle(img_dir)
    y_name = vec2text(y_predict[0])
    for i in range(len(y_name)):
        print("Ԥ��Ϊ��%s"% y_name[i])
    return y_name[0]



if __name__ == '__main__':
    train()
    #evalate()
    #predict()