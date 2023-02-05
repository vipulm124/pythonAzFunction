import logging
import azure.functions as func
from Utilities.QueryDb import QueryData;
import json



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Azure Function triggered for DimOrg')

    try:
        req_body = req.get_json()
        dict=json.loads(req.get_body())
        jsonResponse = QueryData('[dbo].[DimORG]', dict)
        logging.info('Returning json response')
        return func.HttpResponse(jsonResponse)
    
    except Exception as ex:
        logging.error("An exception has occured.")
        logging.error(ex)
        return func.HttpResponse('An exception has occured. Please check logs for details.')
    