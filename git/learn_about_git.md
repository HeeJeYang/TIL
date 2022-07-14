# Today I Learned

## Git

---

- 분산 버전 관리 프로그램 **Git** (**백업, 복구, 협업**)
    - snapshot 방식(기본)과 delta방식(용량이 클 시)
    - Git ≠ Github
- 중앙 집중식 버전 관리는, 중앙 서버가 파괴되면 데이터가 모두 사라진다.
- 1일 1 commit

- Working Directory : 작업 공간
- Staging Area : 가상의 저장 공간
- Commit : 저장소 업로드

### Command

- git config —global user.name username : 유저 등록(최초 1회)
- git config —global user.email email : 이메일 등록(최초 1회)
- git config —global —list : 유저 확인
- git init : 저장소 초기화
    1. master가 뜨는가?
    2. Initialized가 뜨는가?
    3. `ls -a` 를 쳤을 때 .git/이 뜨는가?

### git add → git commit -m → git status(확인)

- **git status** : 상태 확인
- git add : Staging Area로 파일 이동
- git commit -m(메세지 옵션) : 버전 생성
- git log : 커밋 기록 표시
    - —oneline : 기록 한줄 요약
- git checkout <commit ID>: 커밋했던 상태로 이동
- git remote add origin <github https 주소> : 저장소와 다리 연결
- git push origin master : 공유 저장소에 업로드
- U : untracked : 추적되지 않음
- A : index Added : Staging Area에 들어간 상태
- 커밋 ID = 해시값(SHA1)
- **저장 필수!!**

- Staging Area가 존재하는 이유(Git의 꽃)
    1. 내가 원하는 파일만 골라서 Commits에 보낼 수 있다.
    2. 충돌 해결

- 복구 : **reset revert??**

## CLI, GUI

---

- CLI : Command Line Interface
- GUI : Graphic User Interface
- Git을 하기 위한 사전준비
    - CLI → Markdown → Git
- 위로 가기 ≠ 뒤로 가기

### Command

- touch : (파일 생성)
- mkdir : make directory (폴더 생성)
- ls : list segments (목록 표시)
    - -a : all (숨김 표시 옵션)
- cd : change directory (폴더 변경)
    - cd .. : 위로 가기 (부모 폴더로 이동)
- rm : remove (삭제)
    - -r : recursive (폴더 안까지 재귀적으로 지워주는 옵션)
    

### 경로

- 절대경로 : 절대적인 주소
- 상대경로 : 상대적인 위치
    - . : 나
    - .. : 부모
- C드라이브 = root

## Markdown

---

- 텍스트 기반의 경량 **마크업** 언어
- html에서 m = markup
- **마크업** 언어 : 글에 **역할**을 부여하는 것
- **마크다운** : 마크업을 쉽게 만든 것
- 

### Typora

- Ctrl + / : 날 것 그대로 표시
- # : 제목
- - : 순서가 없는 목록
    - tab : sub목록
- 1.  순서가 있는목록
    - tab : sub목록
- ** 문자 ** : 굵게
- *** 문자 *** : 기울임
- ~~ 문자 ~~ : 취소선
- `hello world` : `hello world`
- ```python :

```python
for i in range(5):
print(5)
```

- — : 수평선
- **표** : 마크다운을 쓰는 이유
    - 오른쪽 클릭 → 삽입 → 표 생성
    - Ctrl + Enter : 줄 추가
    - Ctrl + Shift + BackSpace : 줄 삭제