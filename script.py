#Importa boto3 para configuração do client e session

import boto3

#Faz a session da região aws

session = boto3.Session(region_name='us-east-1')

#Armazena os dados ecr na variável ecr

ecr = session.client('ecr')

#Varuavel que armazena o repositories e o repository name

repositories = [repo['repositoryName'] for repo in ecr.describe_repositories()['repositories']]

#print(repositories) #Para ver os nomes dos repositorios listados, basta descomentar e rodar

#Laço de repetição que chama a variável acima e executa o lifecyclepolicy setado

for repo in repositories:

    ecr.put_lifecycle_policy(

        repositoryName = repo,

        lifecyclePolicyText = '{"rules": [{"rulePriority": 1,"description": "Aplica policy de lifecycle","selection": {"tagStatus": "untagged","countType": "sinceImagePushed","countUnit": "days","countNumber": 90},"action": {"type": "expire"}}]}'

    )

#Sobe o serviço da policy automaticamente na aws, pois foi feito dentro de uma SSH na aws
