# app.py

import streamlit as st

# アプリケーションのタイトルを表示
st.title('🚀 Hello Streamlit World!')

# シンプルなテキストを表示
st.write('これは、私がStreamlitを使って作った初めてのWebアプリケーションです。')

# ボタンを追加し、クリックされたときにメッセージを表示
if st.button('メッセージを表示'):
    st.write('ボタンが押されました！開発頑張りマッシュルーム')
