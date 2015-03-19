import pymongo.errors
OperationFailure = pymongo.errors.OperationFailure


class Model(object):

    collection = None

    def __init__(self, result):
        self._fields = result

    def __getattr__(self, attr):
        try:
            return self._fields[attr]
        except KeyError:
            return None

    def __setattr__(self, attr, value):
        if attr in ['id', '_fields']:
            object.__setattr__(self, attr, value)
        else:
            self._fields[attr] = value

    def save(self):
        self._fields['_id'] = self.collection.save(self._fields, safe=True)

    def delete(self):
        self.collection.remove({'_id': self._fields.get('_id', None)})
        self.id = None

    def get_id(self):
        return self._fields.get('_id', None)

    def get_doc(self):
        return self._fields

    id = property(get_id)
    doc = property(get_doc)

    @classmethod
    def get_person_id(cls, person_id):
        if cls.collection:
            person_id = person_id.upper()
            result = cls.collection.find_one(dict(person_id=person_id))
            if result:
                for k, v in result.iteritems():
                    setattr(cls, k, v)
                return cls
        return None

    @classmethod
    def get(cls, spec):
        if cls.collection:
            result = cls.collection.find_one(spec)
            if result:
                for k, v in result.iteritems():
                    setattr(cls, k, v)
                return cls
        return None

    @classmethod
    def set(cls, fields, safe=False):
        cls.collection.update({'_id': cls._id}, {'$set': fields}, safe=safe)
        cls._fields = cls.collection.find_one({'_id': cls._id})

    @classmethod
    def update(cls, fields):
        cls.collection.update({'_id': cls._id}, {"$pull":fields})