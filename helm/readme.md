# How to deploy helm chart

`helm install banks helm/ --create-namespace --namespace banks `

then add api as a secret

`kubectl create secret generic db-data --from-literal=key=<api> -n banks`

check it 

`kubectl get secret db-data -n banks --template={{.data.key}} | base64 -D `

# For update with a tag

`helm upgrade banks helm/ --install --set image.tag=0.0.1`
