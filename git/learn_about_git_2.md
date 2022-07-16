## 복습

---

## Git

- **분산 버전 관리 시스템**
- **백업**
- **복구**
- **협업**
- 3공간
    - Working Directory
    - Staging Area
    - Commits
- **git status** : 3공간의 상태를 나타냄
- git remote add origin : Local과 Remote 사이의 길을 만들어줌
- git push origin master : Remote에 파일 업로드
- **Github :** 공유 저장소
- **Markdown**에서는 **글에 역할을 부여**하기 때문에 본문에 제목 태그를 부여하는 등의
행동을 해서는 안된다.

## TIL

---

## 주의사항

- 바탕화면에서 git init 금지
- git init한 폴더 안에 있는 다른 폴더에 git init하지 않기
- 무조건 Local에서 먼저 변경한 뒤 Remote에 올리기(add → commit → push)
- Typora 업데이트하지 않기

## GIT

- README.md : 프로젝트를 타인에게 설명해주는 파일
- .gitignore : 올리고 싶지 않은 파일 또는 폴더를 숨겨줌
    - .이 붙은 파일은 숨김 파일
    - 기존에 버전 관리를 한 파일은 .gitignore에 넣어도 무시당하지 않는다.
        - **따라서 .gitignore 파일은 맨 처음에 만들어야 한다.**
    - [**gitignore.io**](http://gitignore.io) : gitignore를 편하게 사용하게 만드는 사이트
        - python, windows, visualstudiocode, django
    1. 남에게 보여주면 안되는 보안 파일
    2. 굳이 올리지 않아도 되는 파일(node_module)
- 작업자와 같은 버전을 Remote에 올리려 할 시 충돌 에러가 남. 반드시 git pull로 먼저 버전을 내려받고 작업
- **COMMAND**
    - git clone : 다운로드
        - 없어서 Remote에서 받아오는 것
        - [폴더 생성 → git init → git remote add → 버전, 파일 생성] 작업을 자동으로 실행
    - git pull : 버전 업데이트
        - 있는데 버전을 업데이트하는 것
- git commit convention 분석
    
    

## GIT 충돌(conflict) 시

- master → master[MERGING] 으로 바뀜
- Accept Current Change : 현재 내가 작성한 버전으로 선택
- Accept Incoming Change : Remote에 있는 버전으로 선택
- Accept Both Changes : 둘다 보존
- 싱크를 맞추면 내 버전, 상대 버전, 그리고 합친 버전 모두 Remote에 보존된다.