from Train import Train

params = {
    'EPOCHS': 10,
    'BATCH_SIZE': 64,
    'LEARNING_RATE': 0.0001,
    'DIVIDE_LEARNING_RATE_AT': [5],      # Where the learning rate should be divided at. Count starts from 0

    'TRAIN_FILE': './Data/train.tsv',
    'TEST_FILE': './Data/test.tsv',
    'TRAIN_VAL_RATIO': 0.95,
    'MAX_SENTENCE_WORDS': 25,   # How many words in sentence is to be considered.

    'N_CLASS': 5
}

t = Train(params)
t.train()
t.test()