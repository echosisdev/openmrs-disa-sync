class Constants:
    UUIDS = {
        'encounter_type': 'e2790f68-1d5f-11e0-b929-000c29ad1d07',
        'data_colheita_obs': 'f85e3f84-a255-412a-aa43-40174f69c305',
        'data_pedido_obs': '892a98b2-9c98-4813-b4e5-0b434d14404d',
        'valor_carga_concept': 'e1d6247e-1d5f-11e0-b929-000c29ad1d07',
        'qualidade_carga_question': 'e1da2704-1d5f-11e0-b929-000c29ad1d07',
        'hpt': 'a920a302-8c66-44d4-b4c1-6e4a7c30fabc',
        'form': '8377e4ff-d0fe-44a5-81c3-74c9040fd5f8'
    }

    QUALIDADE_CARGA = {
        'indectetavel': 23814,
        '<400 copias': 23908
    }

    def get_uuids(self):
        return self.UUIDS

    def get_qualidade_carga(self):
        return self.QUALIDADE_CARGA
