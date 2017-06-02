#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re
import io
from subprocess import Popen, PIPE




if os.path.exists('../CHANGELOG.md'):
    os.remove('../CHANGELOG.md')


if not os.path.exists('../CHANGELOG.md'):
    open('../CHANGELOG.md', 'w').close()


def deleteContent (file):
	file.seek(0)
	file.truncate()

with open('../CHANGELOG.md','r') as f:
	f.seek(0)
	first_char = f.read(1)
	if not first_char: 
		previous_date = str("[' 2017-05-20 17:47:16 ']")
	else:
		date = re.findall(r'\d{4}-\d{2}-\d{2}.\d{2}.\d{2}.\d{2}', f.readline())

		converted_date = datetime.datetime.strptime(" ".join(date), '%Y-%m-%d %H:%M:%S')
		seconds_date = converted_date + datetime.timedelta(0,3)

		previous_date = str("[' " + str(seconds_date) + " ']")

f = open('../CHANGELOG.md','r')
changelog_old = f.readlines()

f.close()

f = open('../CHANGELOG.md','a')
deleteContent(f)

# Pull requests mal formateadas
#feature/MON-136  [UPDATE]: crear pipeline para los logs de mesos https://datiobd.atlassian.net/browse/MON-136


f.write('feature/MON-103 [UPDATE]: Borrado de índice en Elastalert https://datiobd.atlassian.net/browse/MON-103\n')
f.write('feature/MON-98 [UPDATE]: Ansible - Search Guard: parametrizar  con el Cambio de user y password a partir de las variables admin_user y admin_pass https://datiobd.atlassian.net/browse/MON-98\n')
f.write('feature/MON-104 [UPDATE]: Logs- Identificar rutas en las que escribe logs el proyecto Kafka  https://datiobd.atlassian.net/browse/MON-104\n')
f.write('feature/MON-105 [UPDATE]: Logs- Identificar rutas en las que escribe logs el proyecto Spark  https://datiobd.atlassian.net/browse/MON-105\n')
f.write('feature/MON-106 [ADD]: Incluir en Argos los logs del proyecto Kafka  https://datiobd.atlassian.net/browse/MON-106\n')
f.write('feature/MON-107 [ADD]: Incluir en Argos los logs del proyecto Spark https://datiobd.atlassian.net/browse/MON-107\n')
f.write('feature/MON-111 [UPDATE]: Estudiar las funciones que proporciona ElastAlert que apliquen a logs https://datiobd.atlassian.net/browse/MON-111\n')
f.write('feature/MON-112 [UPDATE]: Historificación de logs - ¿cómo manejamos el borrado de logs? https://datiobd.atlassian.net/browse/MON-112\n')
f.write('feature/MON-118 [UPDATE]: Estudiar las funciones que proporciona ElastAlert que apliquen a métricas https://datiobd.atlassian.net/browse/MON-118\n')
f.write('feature/MON-119 [UPDATE]: Historificación de métricas - ¿Cómo manejamos el borrado de métricas? https://datiobd.atlassian.net/browse/MON-119\n')
f.write('feature/MON-122 [ADD]: Audit_job https://datiobd.atlassian.net/browse/MON-122\n')
f.write('feature/MON-124 [ADD]: Manejar diferentes versiones de Argos https://datiobd.atlassian.net/browse/MON-124\n')
f.write('feature/MON-127 [ADD]: Manejo de la versión de OpenStack en Argos https://datiobd.atlassian.net/browse/MON-127\n')
f.write('feature/MON-129 [UPDATE]: Seguir documentando mas gráficas de los diferentes dashboards  https://github.com/DatioBD/argos/pull/41 https://datiobd.atlassian.net/browse/MON-129\n')
f.write('feature/MON-131 [UPDATE]: Documentar la creación de gráficas   https://datiobd.atlassian.net/browse/MON-131\n')
f.write('feature/MON-120 [UPDATE]: Métricas - Analizar plugins y detectar cuales nos interesan dentro del PaaS   https://datiobd.atlassian.net/browse/MON-120\n')
f.write('feature/MON-132 [FIX]: El campo admin_password debe llamarse admin_pass   https://datiobd.atlassian.net/browse/MON-132\n')
f.write('feature/MON-136 [FIX]: Añadir creación pipeline tratamiento log ansible   https://datiobd.atlassian.net/browse/MON-136\n')
f.write('feature/MON-137 [FIX]: Añadir opciones de despliegue a Argos - Ansible   https://datiobd.atlassian.net/browse/MON-137\n')
f.write('feature/MON-128 [ADD]: Documentar la creación de gráficas https://datiobd.atlassian.net/browse/MON-128\n')

message = Popen("git log --since={pdate}  --pretty=format:'%b' --grep='Merge pull request'   --date=format:'%Y-%m-%d %H:%M:%S'".format(pdate=previous_date), shell= True, stdout=PIPE).stdout.read()
f.write(message + '\n')

for line in changelog_old:
	f.write(line)

f.close()
