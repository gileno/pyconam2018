# -*- coding: utf-8 -*-

class PyconamPipeline(object):

    def process_item(self, item, spider):
        # Faz alguma limpeza
        # Salva no banco de dados
        return item
