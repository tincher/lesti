import tensorflow as tf
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')


def my_model(features, labels, mode, params):
    # input layer of the net
    net = tf.feature_column.input_layer(features, params['feature_columns'])

    # hidden layers
    for units in params['hidden_units']:
        net = tf.layers.dense(net, units=units, activation=tf.nn.relu)

    # output layer
    logits = tf.layers.dense(net, params['n_classes'], activation=None)

    # prediction mode
    predicted_classes = tf.argmax(logits, 1)
    if mode == tf.estimator.ModeKeys.PREDICT:
        predictions = {
            'class_ids': predicted_classes[:, tf.newaxis],
            'probabilities': tf.nn.softmax(logits),
            'logits': logits
        }
        return tf.estimator.EstimatorSpec(mode, predictions=predictions)

    # loss
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # accuracy
    accuracy = tf.metrics.accuracy(labels=labels, predictions=predicted_classes, name='acc_op')
    metrics = {'accuracy': accuracy}
    tf.summary.scalar('accuracy', accuracy[1])

    # eval mode
    if mode == tf.estimator.ModeKeys.EVAL:
        return tf.estimator.EstimatorSpec(mode, loss=loss, eval_metric_ops=metrics)

    # training
    assert mode == tf.estimator.ModeKeys.TRAIN

    optimizer = tf.train.AdagradOptimizer(learning_rate=0.1)
    train_op = optimizer.minimize(loss, global_step=tf.train.get_global_step())
    return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)


def main(argv):
    # todo
    args = parser.parse_args(argv[1])
