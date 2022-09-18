#!/bin/bash
cd build
if [[ "$(docker image inspect $1 --format='ok')" == "ok" ]]; then
  docker rmi $1
fi
docker build . --no-cache -t $1
# echo $4 | docker login -u $2 --password-stdin $3
# docker push $1

# action config
# jobs:
#   build_image:
#     runs-on: []
#     steps:
#       - uses: actions/checkout@v2
#         with:
#           lfs: 'true'
#       - shell: bash
#         run: |
#           bash ./build.sh \
#           rb-dtr.de.bosch.com/aepjsw/fossid-action:${GITHUB_REF##*/} \
#           ${{env.user}} \
#           ${{env.DTR_url}} \
#           ${{ secrets.EJE1COB_PASS }} \
#           ${{ secrets.PROXY_URL }}