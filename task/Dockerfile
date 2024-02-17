FROM ansible/awx:17.1.0
USER root
ADD launch_awx.sh /usr/bin/launch_awx.sh
ADD launch_awx_task.sh /usr/bin/launch_awx_task.sh
ADD settings.py /etc/tower/settings.py
RUN chmod +rx /usr/bin/launch_awx.sh && \
    chmod +rx /usr/bin/launch_awx_task.sh
USER 1000