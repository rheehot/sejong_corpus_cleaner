from collections import defaultdict
from glob import glob
from .loader import load_a_file
from .utils import data_dir as default_data_dir


def make_eojeol_morphemes_table(table_file_path, data_dir=None,
    convert_lr=False, xsv_as_verb=False, corpus_types=None):

    paths = prepare_data_paths(corpus_types, data_dir)
    raise NotImplemented

def load_counter(file_paths, only_morpheme, convert_lr=False, xsv_as_verb=False):
    counter = defaultdict(int)
    for path in file_paths:
        sents, n_errors = load_a_file(path, remain_not_exists=False)
        for sent in sents:
            for eojeol, morphtags in sent:
                key = (eojeol, tuple(morphtags))
                counter[key] += 1

    # TODO: L-R converting

    if only_morpheme:
        morph_counter = defaultdict(int)
        for (eojeol, morphemes), count in counter.items():
            for morph in morphemes:
                morph_counter[morph] += count
        return morph_counter
    return counter

def make_morpheme_table(table_file_path, data_dir=None,
    convert_lr=False, xsv_as_verb=False, corpus_types=None):

    paths = prepare_data_paths(corpus_types, data_dir)
    raise NotImplemented

def make_lr_corpus(corpus_file_path, data_dir=None,
    xsv_as_verb=False, corpus_types=None):

    paths = prepare_data_paths(corpus_types, data_dir)
    raise NotImplemented

def check_corpus_type(corpus_types):
    if corpus_types is None:
        corpus_types = ['written', 'colloquial']
    for ctype in corpus_types:
        if not (ctype in {'written', 'colloquial'}):
            raise ValueError('Corpus type must be "colloquial" or "written" but {}'.format(ctype))
    return corpus_types

def prepare_data_paths(corpus_types=None, data_dir=None):
    corpus_types = check_corpus_type(corpus_types)
    if data_dir is None:
        data_dir = default_data_dir

    paths = []
    for ctype in corpus_types:
        paths += glob(data_dir + ctype + '/*.txt')

    if len(paths) == 0:
        raise ValueError('File not founded from {}'.format(data_dir))
    return paths
