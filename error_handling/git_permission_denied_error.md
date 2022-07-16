## Error Handling
### git push origin master 시 personal denied 오류 현상
--- 
 SSAFY 수강 중 옆자리 동기 분께서 git push를 하던 중 에러메세지가 뜨셨다. 내용은 이러했다.

![git_permission_denied_error](https://user-images.githubusercontent.com/89143804/179354042-6cb9e437-ef40-43f8-b6c0-241968feda5d.png)

권한이 없다는 것만 이해하여 git 정보에 다른 사람 계정이 등록되어있나 싶어 `git config --global --list`를 요청드렸더니 이상이 없었다.   


결국 프로님께 여쭤봤더니 기존에 로그인한 사용자가 있는 곳으로의 자리이동이 원인이라고 말씀해주셨다.  


> 이는 **Windows 자격증명 페이지**에 들어간 뒤 **기존의 git 자격증명을 제거**하고 **재실행**하여 해결하였다.