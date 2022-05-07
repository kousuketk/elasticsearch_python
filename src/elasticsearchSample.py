from elasticsearch import Elasticsearch


class elasticsearchSample:
    def __init__(self):
        self.client = Elasticsearch("http://localhost:9200")

    def __del__(self):
        self.client.close()

    def get_indices(self):
        return self.client.cat.indices(index="*", h="index").splitlines()

    def get_mappings(self):
        return self.client.indices.get_mapping()

    def get_counts_by_index(self, idx):
        return self.client.count(index=idx)

    def create_index(self, idx):
        return self.client.indices.create(index=idx)

    def get_mapping_by_index(self, idx):
        return self.client.indices.get_mapping(index=idx)

    def is_exists_by_index(self, idx):
        return self.client.indices.exists(index=idx)

    def insert_document(self, idx, id, doc):
        return self.client.create(index=idx, id=id, body=doc)

    def search_all_by_index(self, idx):
        return self.client.search(index=idx)
