from elasticsearchSample import elasticsearchSample


def get_info_sample(obj):
    indices = obj.get_indices()
    print("----------- indices -----------")
    print(indices)
    # mappings = obj.get_mappings()
    # print(mappings)
    idx = "students"
    student_mapping = obj.get_mapping_by_index(idx)
    print("----------- student_mapping -----------")
    print(student_mapping)
    print("----------- students idx is exists? -----------")
    print(obj.is_exists_by_index(idx))
    print("----------- students100000 idx is exists? -----------")
    print(obj.is_exists_by_index("students100000"))
    print("----------- count students -----------")
    print(obj.get_counts_by_index(idx))


def insert_sample(obj):
    idx = "students"
    doc = {"name": "Taro", "age": 36, "email": "taro3@test.com"}
    id = 3
    obj.insert_document(idx, id, doc)


def search_sample(obj):
    idx = "students"
    result = obj.search_all_by_index(idx)
    for document in result["hits"]["hits"]:
        print(document["_source"])


def main():
    es = elasticsearchSample()
    get_info_sample(es)
    # insert_sample(es)
    search_sample(es)


if __name__ == "__main__":
    main()
