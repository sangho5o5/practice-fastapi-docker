# practice-fastapi-docker
practice ML deployment with fastapi and docker  
fastapi로 SpaCy의 Named Entity Recognition을 서비스할 수 있게 만들고  
docker로 이미지를 만들어서 배포가 가능하게 연습해 보았다.  
참고 [링크](https://www.youtube.com/watch?v=Maj9v-Ev7-4)

- 저자는 poetry로 가상환경관리를 했지만 익숙하지 않아 해당부분은 모두 제거했다.
- 그래서 dockerfile에선 pip으로 별도로 spacy,fastapi,uvicorn을 설치한다.
- 익숙한 Anaconda로 가상환경과 의존성관리를 추가하면 좋은 연습이 될것 같다.
