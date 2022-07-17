# **Today I Learned**

하루에 하나씩 배운 것을 올리는 곳입니다.

![TIL](https://user-images.githubusercontent.com/89143804/179355404-cd895f97-8aac-461b-aa16-3167b49f1765.png)


## **Commit Message Rule**
---

**1. Github commit 메세지 규칙의 필요성**

- 편리한 과거의 기록 추적
- 이슈를 함께 작성하면서 이슈와 관련된 진행 사항을 확인 가능
  
**2. Commit 메세지 작성 요령**

>타입(Type): 제목(Subject)
>
>본문(Body) - 선택 사항
>
>꼬리말(Footer) - Issue Tracker ID

**2.1. 타입(Type)**   

- Feat - 새로운 기능 추가  
- Fix - 버그 및 오타 수정  
- Docs - 문서 및 파일 (추가, 수정, 삭제)  
- Style - 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없는 경우)  
- Chore - 기타 변경사항  


**2.2. 제목(Subject)Permalink**  

- 제목은 50자를 넘기지 않고, 마침표를 붙이지 않습니다.  
- 제목에는 commit 타입을 함께 작성합니다.  
- 본문을 생략하는 제목은 `(주제) 관련 (내용)`의 양식을 적용합니다.
- 과거 시제를 사용하지 않고 명령조로 작성합니다.  
- 제목과 본문은 한 줄 띄워 분리합니다.  
- 제목의 첫 글자는 반드시 대문자로 씁니다.  
- 제목이나 본문에 이슈 번호(가 있다면) 붙여야 합니다.  

※ 타입(Type) - 제목(Subject) 예시  

> Docs: git 관련 Error Handling 추가

**2.3. 본문(Body)**
- 선택 사항이기에 모든 commit에 본문 내용을 작성할 필요는 없습니다.
- 한 줄에 72자를 넘기면 안 됩니다.
- 어떻게(How)보다 무엇을, 왜(What, Why)에 맞춰 작성합니다.
- 설명뿐만 아니라, commit의 이유를 작성할 때에도 씁니다.

※ 본문(Body) 예시

> Docs : python 관련 command 파일 이름 변경
> 
> 파일 이름의 통일성을 위한 이름 변경  
>   ― command -> commands  

**2.4. 꼬리말(Footer)**
- 선택 사항이므로 모든 commit에 꼬리말을 작성할 필요는 없습니다.
- Issue tracker ID를 작성할 때 사용합니다.

>해결: 이슈 해결 시 사용  
>관련: 해당 commit에 관련된 이슈 번호  
>참고: 참고할 이슈가 있는 경우 사용  
>
>해결: #123  
>관련: #321  
>참고: #222

※ 작성할 Commit 메세지 예시

> Docs : python 관련 command 파일 이름 변경
> 
> 파일 이름의 통일성을 위한 이름 변경  
>   ― command -> commands  
>
> 참고: #57

***

본문 출처 : https://junhyunny.github.io/information/github/git-commit-message-rule/  
이미지 출처 : https://velog.io/@richard/TIL-5-Html-%EA%B8%B0%EC%B4%88