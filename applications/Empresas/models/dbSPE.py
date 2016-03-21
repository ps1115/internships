# -*- coding: utf-8 -*-
dbSPE = DAL('mysql://root:root@localhost:3306/pasantiasnuevo', pool_size=0,migrate=False)

def captcha_field(request=request):
    from gluon.tools import Recaptcha2
    w = lambda x,y: Recaptcha2(request,
                              '6Lcg5hoTAAAAADfqPDXf4htFpyjqkBGRID3KiLEP',
                              '6Lcg5hoTAAAAANYiBEtWC1NSG5nEMZcHMgC4_eIT')

    return Field('captcha', 'string', widget=w, default='ok')
