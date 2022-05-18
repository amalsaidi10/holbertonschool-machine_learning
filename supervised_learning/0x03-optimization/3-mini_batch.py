#!/usr/bin/env python3
"""
    Mini-Batch Training Module
"""
import tensorflow.compat.v1 as tf
shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(
        X_train, Y_train, X_valid, Y_valid, batch_size=32,
        epochs=5, load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """
        Build, trains and saves a neural network classifier
        Args:
            X_train: training input data
            Y_train: training labels data
            X_valid: validation input data
            Y_valid: validation labels data
            batch_size: number of data points in each batch
            epochs: number of times the training data is passed
                    through the network
            load_path: path to load the model
            save_path: path to save the model
        Returns:
            save_path: path to save the model
    """

    with tf.Session() as session:
        saver = tf.train.import_meta_graph(load_path + '.meta')
        saver.restore(session, load_path)

        # Restore variables
        x = tf.get_collection('x')[0]
        y = tf.get_collection('y')[0]
        accuracy = tf.get_collection('accuracy')[0]
        loss = tf.get_collection('loss')[0]
        train_op = tf.get_collection('train_op')[0]

        training_data = {x: X_train, y: Y_train}
        validation_data = {x: X_valid, y: Y_valid}

        for epoch in range(epochs + 1):
            train_accuracy, train_cost = session.run(
                [accuracy, loss], feed_dict={x: X_train, y: Y_train}
            )
            valid_accuracy, valid_cost = session.run(
                [accuracy, loss], feed_dict={x: X_valid, y: Y_valid}
            )

            print("After {} epochs:".format(epoch))
            print("\tTraining Cost: {}".format(train_cost))
            print("\tTraining Accuracy: {}".format(train_accuracy))
            print("\tValidation Cost: {}".format(valid_cost))
            print("\tValidation Accuracy: {}".format(valid_accuracy))

            if epoch == epochs:
                break

            # Shuffle the training data
            x_shuffle, y_shuffle = shuffle_data(X_train, Y_train)

            # Loop over the training data
            for step in range(steps):
                start = batch_size * step
                end = batch_size * (step + 1)

                # Get X_batch and Y_batch
                x_batch = x_shuffle[start:end]
                y_batch = y_shuffle[start:end]

                # Train your model
                session.run(
                    train_op,
                    feed_dict={x: x_batch, y: y_batch}
                )

                if (step + 1) % 100 == 0:
                    step_accuracy, step_cost = session.run(
                        [accuracy, loss], feed_dict={x: x_batch, y: y_batch}
                    )

                    print("\tStep {}:".format(step))
                    print("\t\tCost: {}".format(step_cost))
                    print("\t\tAccuracy: {}".format(step_accuracy))

        return store.save(session, save_path)
  
