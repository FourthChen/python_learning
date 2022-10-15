# # import slate
# #
# # pdf='E:/python学习/数据分析/数据/EN-FINAL Table 9.pdf'
# #
# # with open(pdf) as f:
# #     doc=slate.PDF(f)
# #
# # for page in doc[:2]:
# #     print(type(page))
#
# import pprint
# pdf_txt='E:/python学习/数据分析/数据/en-final-table9.txt'
# openfile=open(pdf_txt,'r',encoding='utf-8')
#
# # for line in openfile:
# #     print(line)
#
#
# # country_line=total_line=False
# # for line in openfile:
# #      if country_line or total_line:
# #          print('%r'%line)
# #      if line.startswith('and areas'):
# #          country_line=True
# #      elif country_line:
# #          if line=='\n':
# #              country_line=False
# #      if line.startswith('total'):
# #          total_line=True
# #      elif total_line:
# #          if line=='\n':
# #              total_line=False
#
# double_lined_countries=[
#     'Bolivia (Plurinational',
#     # 'Democratic People’s',
#     # 'Democratic Republic',
#     # 'Venezuela (Bolivarian',
#     'Republic of Moldova'
# ]
#
#
# def turn_on_off(line,status,prev_line,start,end='\n'):  #有默认值的参数要放在最后
#     '''
#     这个函数用于检查该行是否以特定值开始/结束。
#     如果该行确实以特定值开始/结束，则状态设为开/关（真/假）
#     :param line:
#     :param status:
#     :param start:
#     :param end:
#     :return:
#     '''
#     if line.startswith(start):
#         status=True
#     elif status:
#         if line ==end and prev_line !='and areas':
#             status=False
#     return status
# def clean(line):
#     '''
#     清洗代码中的换行符、空格以及其他特殊符号
#     :param line:
#     :return:
#     '''
#     line=line.strip('\n').strip()
#     line=line.replace('\xe2\x80\x93','-')
#     line=line.replace('\xe2\x80\x99','\'')
#     # line=line.replace('')
#     return line
# counties=[]
# totals=[]
# country_line=total_line=False
# previous_line=''
# for line in openfile:
#      if country_line:
#          if previous_line in double_lined_countries:
#              line=' '.join([clean(previous_line),clean(line)])
#              counties.append(clean(line))
#      # if total_line:
#          elif line not in double_lined_countries:
#              counties.append(clean(line))
#      elif total_line:
#          if len(line.replace('\n','').strip()) >0:
#             totals.append(clean(line))
#          # totals.append(clean(line))
#      # if country_line or total_line:
#      #     print('%r'%line)
#      country_line=turn_on_off(line,country_line,'and areas',previous_line)
#      total_line=turn_on_off(line,total_line,'total',previous_line)
#      previous_line=line
#
# test_data=dict(zip(counties,totals))
# pprint.pprint(test_data)


# _*_coding:utf-8_*_

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfpage import PDFTextExtractionNotAllowed


def parse(Path, Save_name):
    parser = PDFParser(Path)
    document = PDFDocument(parser)

    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open('%s' % (Save_name), 'a') as f:
                        results = x.get_text().encode('utf-8')
                        f.write(results + "\n")


if __name__ == '__main__':
    Path = open(r'C:\Users\24702\Desktop\密码学密码算法与协议 第2版 [郑东 编著] 2014年版.pdf', 'rb',encoding='utf-8')
    parse(Path, '1.txt')