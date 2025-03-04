# -*- coding: utf-8 -*-

# 创建表
from domain_admin.log import logger
from domain_admin.model.base_model import db
from domain_admin.model import domain_model
from domain_admin.model import group_model
from domain_admin.model import system_model
from domain_admin.model import user_model
from domain_admin.model import log_scheduler_model
from domain_admin.model import notify_model

tables = [
    (system_model.SystemModel, system_model.init_table_data),
    (domain_model.DomainModel, None),
    (group_model.GroupModel, None),
    (user_model.UserModel, user_model.init_table_data),
    (log_scheduler_model.LogSchedulerModel, None),
    (notify_model.NotifyModel, None),
]


def init_database():
    db.connect()

    for model, init_func in tables:
        if not model.table_exists():
            logger.debug('create table: %s', model._meta.table_name)
            model.create_table()

            if init_func:
                init_func()

    db.close()
