# coding=utf-8
from __future__ import unicode_literals

from django.core.exceptions import FieldError

from commons.exeptions import BadRequestError


class FilterMixin(object):
    """
    Фильтрует queryset на основе параметров переданых в строке запроса
        ?id=1&name=name
    Преобразует в строку фильра:
        id=1, name=name
    Возвращает отфильтрованые объекты которые удовлетворяют условию
    """

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if not params:
            return super(FilterMixin, self).filter_queryset(queryset)
        try:
            return queryset.filter(**params.dict())
        except FieldError as e:
            raise BadRequestError("Не корректные параметры для фильтрации. " \
                                  "Описание ошибки:%s" % e.message)
