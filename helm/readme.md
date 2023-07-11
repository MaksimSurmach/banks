# How to deploy helm chart

`helm install banks helm/ --create-namespace --namespace banks `

then add api as a secret

`kubectl create secret generic DB_USER --from-literal=key=<api> -n banks`

check it 

`kubectl get secret DB_USER -n banks --template={{.data.key}} | base64 -D `

# For update with a tag

`helm upgrade banks helm/ --install --set image.tag=0.0.1`
