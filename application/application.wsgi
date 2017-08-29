# -*- coding: utf-8 *-*
 
import os, sys
 
sys.path.append('/var/www/app')
 
def application(environ, start_response):
    from application.modulos_python.serieF import leer
    output = leer()
    start_response('200 OK', 
               [('Content-Type', 
                 'text/html; charset=utf-8')])
 
    return output
