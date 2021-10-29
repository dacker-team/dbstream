import datetime
import uuid


def generate_dck_info(row_data, batch_id=None):
    result = []
    _now = datetime.datetime.now()
    for row in row_data:
        if not row.get('__dck_id___'):
            row['__dck_id___'] = str(uuid.uuid4())
        if not row.get('__dck_inserted_at___'):
            row['__dck_inserted_at___'] = _now
        if batch_id and not row.get('__dck_batch_id___'):
            row['__dck_batch_id___'] = batch_id
        result.append(row)
    return result
