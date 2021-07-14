
def main():
    '''
    url 에 저장된 웹 페이지 주소에서 도메인을 출력하라.

    url = "http://sharebook.kr"
    url = "https://korea.co.kr"


    출력:
        kr

    '''
    url = "http://sharebook.kr"
    url2 = "https://korea.co.kr"
    url3 = "https://naver.com"

    domain = None
    ####### 구현 시작 ################
    domain = url[url.rfind('.') + 1:]
    domain2 = url2[url2.rfind('.') + 1:]
    domain3 = url3[url3.rfind('.') + 1:]

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(domain)
    print(domain2)
    print(domain3)
    print("-------------------------------------------------------------------------------")


## 메인 함수 호출 ##
if __name__ == "__main__":
    main()
