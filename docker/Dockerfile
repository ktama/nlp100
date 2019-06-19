FROM ubuntu
RUN sed -i -e 's%http://.*.ubuntu.com%http://ftp.jaist.ac.jp/pub/Linux%g' /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y install libc6 python-dev gcc make g++ wget tar
RUN wget -O CRF++-0.58.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ'
RUN tar xvzf CRF++-0.58.tar.gz
RUN cd CRF++-0.58
# RUN ./configure
# RUN make
# RUN make install
# RUN cd ../
# RUN wget -O mecab-0.996.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE'
# RUN tar xvzf mecab-0.996.tar.gz
# RUN cd mecab-0.996
# RUN ./configure
# RUN make
# RUN make check
# RUN make install
# RUN cd ../
# RUN wget -O mecab-ipadic-2.7.0-20070801.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM'
# RUN tar xvzf mecab-ipadic-2.7.0-20070801.tar.gz
# RUN cd mecab-ipadic-2.7.0-20070801
# RUN ./configure -with-charset=utf-8 –enable-utf8-only
# RUN make
# RUN make install
# RUN cd ../

# 過去の
# RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
# RUN cd mecab-ipadic-neologd
# shのsudoを削除＋yes入力が必要なので不可
# RUN ./bin/install-mecab-ipadic-neologd -n

