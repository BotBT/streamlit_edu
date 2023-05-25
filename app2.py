import streamlit as st

def main():
    st.title('앱 대시보드')

    name = '홍길동'

    print('제 이름은 {}입니다.'.format(name)) # 출력은 터미널의 찍히는 출력 = 결과값 이다.
    
    st.text('제 이름은 {}입니다.'.format(name)) # {}포맷팅을 사용하여 name 변수를 중괄호 안에 나타나게 활용.

    st.header('이 영역은 헤더 영역')

    st.subheader('이 영역은 서브헤드 입니다.')

    st.success('성공했을때 나타내고 싶은 문장')

    st.warning('경고하고 싶을때 문장')

    st.info('알림을 주고 싶을때')

    st.error('문제가 발생했을을 알려주고 싶을때')

    st.help(range)


if __name__ == '__main__':
    main()