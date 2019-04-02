from fastai.text import *
from fastai.lm_rnn import get_rnn_classifer
import html
from nltk import word_tokenize
BOS = 'xbos'  # beginning-of-sentence tag
FLD = 'xfld'  # data field tag

#Path to the news dataset
PATH=Path('news/')
class Tokenizer():
    """
    Patching the fastai tokenizer
    """
    def __init__(self, lang='en'):
        pass

    def spacy_tok(self,x):
        return word_tokenize(x)

    def proc_text(self, s):
        return self.spacy_tok(s)

    @staticmethod
    def proc_all(ss, lang):
        tok = Tokenizer(lang)
        return [tok.proc_text(s) for s in ss]

    @staticmethod
    def proc_all_mp(ss, lang='en'):
        ncpus = num_cpus()//2
        with ProcessPoolExecutor(ncpus) as e:
            return sum(e.map(Tokenizer.proc_all, ss, [lang]*len(ss)), [])
CLAS_PATH=Path('news/news_clas/')
CLAS_PATH.mkdir(exist_ok=True)

LM_PATH=Path('news/news_lm/')
LM_PATH.mkdir(exist_ok=True)
data = pd.read_csv('news/all_news.csv').values
trn_texts,trn_labels = data[::,0],data[::,1]
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(trn_labels)
trn_labels = le.transform(trn_labels)
label2idx = dict()
for i,label in enumerate(le.classes_):
    label2idx[label] = i
np.save("news/news_clas/l2i.npy",label2idx)
trn_texts,val_texts,trn_labels,val_labels = sklearn.model_selection.train_test_split(trn_texts,trn_labels,test_size=0.1)
col_names = ['labels','text']
np.random.seed(42)
trn_idx = np.random.permutation(len(trn_texts))
val_idx = np.random.permutation(len(val_texts))
trn_texts = trn_texts[trn_idx]
val_texts = val_texts[val_idx]

trn_labels = trn_labels[trn_idx]
val_labels = val_labels[val_idx]
df_trn = pd.DataFrame({'text':trn_texts, 'labels':trn_labels}, columns=col_names)
df_val = pd.DataFrame({'text':val_texts, 'labels':val_labels}, columns=col_names)
df_trn.to_csv(CLAS_PATH/'train.csv', header=False, index=False)
df_val.to_csv(CLAS_PATH/'test.csv', header=False, index=False)
trn_texts,val_texts = sklearn.model_selection.train_test_split(np.concatenate([trn_texts,val_texts]), test_size=0.1)
len(trn_texts), len(val_texts)

df_trn = pd.DataFrame({'text':trn_texts, 'labels':[0]*len(trn_texts)}, columns=col_names)
df_val = pd.DataFrame({'text':val_texts, 'labels':[0]*len(val_texts)}, columns=col_names)

df_trn.to_csv(LM_PATH/'train.csv', header=False, index=False)
df_val.to_csv(LM_PATH/'test.csv', header=False, index=False)
chunksize=24000
re1 = re.compile(r'  +')

def fixup(x):
    x = x.replace('#39;', "'").replace('amp;', '&').replace('#146;', "'").replace(
    'nbsp;', ' ').replace('#36;', '$').replace('\\n', "\n").replace('quot;', "'").replace(
    '<br />', "\n").replace('\\"', '"').replace('<unk>','u_n').replace(' @.@ ','.').replace(
    ' @-@ ','-').replace('\\', ' \\ ').replace('\u200d','').replace('\xa0',' ').replace(
    '\u200c','').replace('“',' ').replace('”',' ').replace('"',' ').replace('\u200b','')
    x = re.sub('[\(\[].*?[\)\]]', '', x)
    x = re.sub('<[^<]+?>', '', x)
    x = re.sub('[A-Za-z]+','ENG ', x)
    x = re.sub(r'\d+.?(\d+)?','NUM ',x).replace("(","").replace(")","")
    return re1.sub(' ', html.unescape(x))
def get_texts(df, n_lbls=1):
    labels = df.iloc[:,range(n_lbls)].values.astype(np.int64)
    texts = f'\n{BOS} {FLD} 1 ' + df[n_lbls].astype(str)
    for i in range(n_lbls+1, len(df.columns)): texts += f' {FLD} {i-n_lbls} ' + df[i].astype(str)
    texts = list(texts.apply(fixup).values)

    tok = Tokenizer().proc_all_mp(partition_by_cores(texts))
    return tok, list(labels)
def get_all(df, n_lbls):
    tok, labels = [], []
    for i, r in enumerate(df):
        print(i)
        tok_, labels_ = get_texts(r, n_lbls)
        tok += tok_;
        labels += labels_
    return tok, labels
df_trn = pd.read_csv(LM_PATH/'train.csv', header=None, chunksize=chunksize)
df_val = pd.read_csv(LM_PATH/'test.csv', header=None, chunksize=chunksize)
tok_trn, trn_labels = get_all(df_trn, 1)
tok_val, val_labels = get_all(df_val, 1)
print(tok_trn[0])
(LM_PATH/'tmp').mkdir(exist_ok=True)
np.save(LM_PATH/'tmp'/'tok_trn.npy', tok_trn)
np.save(LM_PATH/'tmp'/'tok_val.npy', tok_val)
tok_trn = np.load(LM_PATH/'tmp'/'tok_trn.npy')
tok_val = np.load(LM_PATH/'tmp'/'tok_val.npy')
print(tok_trn[5])
' '.join(tok_trn[5])

freq = Counter(p for o in tok_trn for p in o)
freq.most_common(25)
max_vocab = 60000
min_freq = 1
itos = [o for o,c in freq.most_common(max_vocab) if c>min_freq]
itos.insert(0, '_pad_')
itos.insert(0, '_unk_')
stoi = collections.defaultdict(lambda:0, {v:k for k,v in enumerate(itos)})
len(itos)
trn_lm = np.array([[stoi[o] for o in p] for p in tok_trn])
val_lm = np.array([[stoi[o] for o in p] for p in tok_val])

np.save(LM_PATH/'tmp'/'trn_ids.npy', trn_lm)
np.save(LM_PATH/'tmp'/'val_ids.npy', val_lm)
pickle.dump(itos, open(LM_PATH/'tmp'/'itos.pkl', 'wb'))
trn_lm = np.load(LM_PATH/'tmp'/'trn_ids.npy')
val_lm = np.load(LM_PATH/'tmp'/'val_ids.npy')
itos = pickle.load(open(LM_PATH/'tmp'/'itos.pkl', 'rb'))
vs=len(itos)
vs,len(trn_lm)
em_sz,nh,nl = 400,1150,3
PATH2 = Path('news/')
PRE_PATH = Path("wiki/ml/")
PRE_LM_PATH = PRE_PATH/'models/fwd_.h5'
wgts = torch.load(PRE_LM_PATH, map_location=lambda storage, loc: storage)
enc_wgts = to_np(wgts['0.encoder.weight'])
row_m = enc_wgts.mean(0)

itos2 = pickle.load((PRE_PATH/'tmp/itos.pkl').open('rb'))
stoi2 = collections.defaultdict(lambda:-1, {v:k for k,v in enumerate(itos2)})





