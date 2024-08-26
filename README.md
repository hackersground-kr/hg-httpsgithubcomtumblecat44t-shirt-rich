# `티셔츠 부자되기` - `diery`

해커그라운드 해커톤에 참여하는 `티셔츠 부자되기` 팀의 `diery`입니다.

## 참고 문서

> 아래 두 링크는 해커톤에서 앱을 개발하면서 참고할 만한 문서들입니다. 이 문서들에서 언급한 서비스 이외에도 더 많은 서비스들이 PaaS, SaaS, 서버리스 형태로 제공되니 참고하세요.

- [순한맛](./REFERENCES_BASIC.md)
- [매운맛](./REFERENCES_ADVANCED.md)

## 제품/서비스 소개

<!-- 아래 링크는 지우지 마세요 -->
[제품/서비스 소개 보기](TOPIC.md)
<!-- 위 링크는 지우지 마세요 -->

## 오픈 소스 라이센스

<!-- 아래 링크는 지우지 마세요 -->
[오픈소스 라이센스 보기](./LICENSE)
<!-- 위 링크는 지우지 마세요 -->

## 설치 방법

> **아래 제공하는 설치 방법을 통해 심사위원단이 여러분의 제품/서비스를 실제 Microsoft 애저 클라우드에 배포하고 설치할 수 있어야 합니다. 만약 아래 설치 방법대로 따라해서 배포 및 설치가 되지 않을 경우 본선에 진출할 수 없습니다.**

### 사전 준비 사항

> **여러분의 제품/서비스를 Microsoft 애저 클라우드에 배포하기 위해 사전에 필요한 준비 사항들을 적어주세요.**

react, vscode, spring boot, Python 3.9, flask 설치, 애저계정

## 시작하기

vscode 를 다운로드 합니다.

vscode에 들어간 후 열기를 누르고 새로운 파일을 누른 후 azurewebapp 파일을 생성합니다. 열기를 눌러 파일에 들어갑니다. 

작성자를 신뢰합니다.

위의 터미널에서 새 터미널을 클릭합니다.

git clone https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart 복사하고 붙혀넣기합니다.

cd msdocs-python-flask-webapp-quickstart 복사 붙혀넣기합니다.

윈도우라면 
py -m venv .venv
.venv\scripts\activate 복사붙혀넣기하고 

맥이라면 
python3 -m venv .venv
source .venv/bin/activate 이걸 복사붙혀넣기합니다.

종속성 다운로드 합니다. 밑의 코드를 터미널에 복사붙혀넣기하십시오
pip install -r requirements.txt

앱을 실행합니다 밑의 코드를 터미널에 복사붙혀넣기하십시오
flask run

애저 포털에 들어갑니다.  아래 링크에 들어가십시오
https://azure.microsoft.com/ko-kr/get-started/azure-portal/

애저 계정에 로그인합니다.

지침	스크린샷
Azure Portal에서 다음을 수행합니다.
Azure Portal 맨 위에 있는 검색 창에 앱 서비스를 입력합니다.
검색 창 아래에 표시되는 메뉴의 서비스 제목 아래에서 App Services라는 레이블이 지정된 항목을 선택합니다.
위쪽 도구 모음의 검색 창을 사용하여 Azure에서 App Services를 찾는 방법을 보여주는 스크린샷
App Services 페이지에서 + 만들기를 선택한 다음 드롭다운 메뉴에서 + 웹앱을 선택합니다.	Azure Portal의 App Service 페이지에서 [만들기] 단추의 위치를 보여주는 스크린샷
웹앱 만들기 페이지에서 다음과 같이 양식을 작성합니다.
  리소스 그룹 → 새로 만들기를 선택하고 이름으로 msdocs-python-webapp-quickstart를 사용합니다.
  이름 → msdocs-python-webapp-quickstart-XYZ를 선택합니다. XYZ는 임의의 세 문자입니다. 이 이름은 Azure에서 고유해야 합니다.
  런타임 스택 → Python 3.9를 선택합니다.
  지역 → 가까운 Azure 지역을 선택합니다.
  App Service 요금제 → 가격 책정 요금제에서 가격 책정 요금제 탐색을 선택하여 다른 App Service 요금제를 선택합니다.
  Azure Portal에서 새 App Service를 만드는 양식을 채우는 방법을 보여주는 스크린샷
  App Service 요금제는 앱에서 사용할 수 있는 리소스 수(CPU/메모리)와 해당 리소스의 비용을 제어합니다.

이 예제의 경우 개발/테스트에서 B1 기본 요금제를 선택합니다. B1 기본 요금제는 Azure 계정에 요금을 소액 부과하지만 F1 무료 요금제보다 더 나은 성능을 발휘하려면 사용하는 것이 좋습니다.

완료되면 선택을 선택하여 변경 내용을 적용합니다.	Azure Portal에서 기본 App Service 요금제를 선택하는 방법을 보여주는 스크린샷
기본 웹앱 만들기 페이지의 화면 아래쪽에서 검토 + 만들기를 선택합니다.

그러면 [검토] 페이지로 이동됩니다. 그런 다음, 만들기를 선택하여 App Service를 만듭니다.	Azure Portal에서 [검토 + 만들기] 단추의 위치를 보여주는 스크린샷

애플리케이션의 App Service로 이동합니다.
화면 맨 위에 있는 검색 상자에 App Service의 이름을 입력합니다.
리소스 제목에서 App Service를 선택하여 탐색합니다.

App Service에 대한 페이지에서 다음을 수행합니다.
화면 왼쪽의 메뉴에서 배포 센터를 선택합니다.
원본이라는 레이블이 지정된 드롭다운 목록에서 로컬 Git을 선택합니다.
저장을 선택합니다.

저장하면 페이지가 새로 고쳐지고 원격 Git 리포지토리의 주소가 표시됩니다.

이 값은 이후 단계에서 Git 원격을 설정하는 데 사용되므로 Git Clone Uri의 값을 복사합니다.

배포 센터 페이지에서 다음을 수행합니다.
로컬 Git/FTPS 자격 증명 탭으로 이동합니다.
애플리케이션 범위 자격 증명에서 로컬 Git 사용자 이름과 암호를 찾습니다.
원격 리포지토리에 코드를 배포할 때 이러한 자격 증명을 일시적으로 복사할 수 있도록 이 화면을 열어두세요. $로 시작하는 로컬 git 사용자 이름(예: $msdocs-python-webapp-quickstart-123)을 복사해야 합니다.
처음으로 원격 Git 리포지토리에 코드를 푸시하는 경우 원격 리포지토리에 인증하려면 이러한 자격 증명이 필요합니다.

다음으로, 애플리케이션의 루트 디렉터리에서 이전 단계에서 가져온 Azure 원격의 Git URL을 사용하여 Azure를 가리키는 Git 원격을 구성합니다.

Bash  터미널에 아래 코드를 복붙하십시오
git remote add azure <git-deployment-url>

이제 방금 구성한 Git 원격을 사용하여 로컬 Git 리포지토리에서 Azure로 코드를 푸시할 수 있습니다. App Service의 기본 배포 분기는 master이지만, 많은 Git 리포지토리가 master에서 main으로 이동하고 있습니다. 아래와 같이 로컬 분기 이름에서 원격 분기 이름으로 매핑을 푸시에서 지정하거나 앱 설정DEPLOYMENT_BRANCH을 구성할 수 있습니다.

Bash 터미널에 아래코드 복붙하십시오
git push azure main:master

http://<app-name>.azurewebsites.net 들어가면 끝

> **여러분의 제품/서비스를 Microsoft 애저 클라우드에 배포하기 위한 절차를 구체적으로 나열해 주세요.**
