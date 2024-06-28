

def create_api_response(status,success_count=None,failed_count=None, data=None, error=None,message=None,file_source=None,file_name=None):
    """
    API에 전송할 응답을 생성하는 도우미 함수입니다. 이 함수는 API에 전송할 JSON 응답을 생성합니다.
    
    Args:
        status: API 호출의 상태. 이 모듈의 상수 중 하나여야 합니다.
        data: API 호출에 의해 반환된 데이터.
        error: API 호출에 의해 반환된 오류.
        success_count: 성공적으로 처리된 파일 수.
        failed_count: 처리에 실패한 파일 수.
    
    Returns:
        상태, 데이터 및 오류(있는 경우)를 포함하는 딕셔너리      

    """
    response = {"status": status}

    # Set the data of the response
    if data is not None:
      response["data"] = data

    # Set the error message to the response.
    if error is not None:
      response["error"] = error
    
    if success_count is not None:
      response['success_count']=success_count
      response['failed_count']=failed_count
    
    if message is not None:
      response['message']=message

    if file_source is not None:
      response['file_source']=file_source

    if file_name is not None:
      response['file_name']=file_name
      
    return response