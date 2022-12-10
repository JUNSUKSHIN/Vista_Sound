# Vista_Sound

# 설치 방법

## 유니티 프로젝트 설치 방법

1. Vista_sound 리포리토리를 다운로드 하거나 clone하여 로컬 저장소에 저장합니다.
2. XR-인터렉션 툴킷을 아래의 링크에서 다운로드 합니다.
    1. https://github.com/Unity-Technologies/XR-Interaction-Toolkit-Examples
4. 유니티를 설치하고 XR-인터렉션 툴킷의 프로젝트를 엽니다.
    1. [Unity Hub](https://unity3d.com/get-unity/download) 에서 유니티 2021.3.15f 이상의 버젼을 설치합니다.
    1.  **Projects** 탭에서 **Add**를 선택합니다.
    1. XR-인터렉션 툴킷을 선택합니다.
5. `Assets` 경로에 `Camera_pose_estimation` 폴더의 파일들을 복사하여 붙여 넣습니다.
6. 자신의 환경에 맞는 XR device 설정을 합니다.
    1. 유니티 메뉴에서 **Edit &gt; Project Settings &gt; XR Plug-in Management**로 진입한 후 자신의 환겨에 맞춰 설정합니다.
7. 유니티의 재생 버튼을 누르면 좌표 녹화가 시작되며 재생이 끝나면 `Assets/position_log.txt`가 생성된 것을 볼 수 있습니다.

## 데이터 전처리 블록 설치 방법

