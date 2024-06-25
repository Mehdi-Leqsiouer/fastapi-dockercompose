# Fast API with docker-compose demo

The Inference Pipeline is made of components that are developed separately. The inference code will call these components.

```
fastapi-dockercompos
  ├── src
        └── endpoints                 <== Contain all routers
            └── common.py                <==  Common endpoints (health check etc)
            ├── knowledgebas_router.py   <==  Endpoints to query the table knowledgebase
            ├── ...
        ├── inference_pipeline.py     <== the pipeline code
        └── requirements.txt          <== modules to install in CF not present in Docker image
  ├── terraform              <== tf files
  ├── tests                             <== the config files for the cloud function


```
