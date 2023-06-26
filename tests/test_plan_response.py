# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

from google.protobuf.json_format import Parse

from cerbos.response.v1 import response_pb2
from cerbos.engine.v1 import engine_pb2


def test_operand_decode():
    data = """
{
  "kind": "KIND_CONDITIONAL",
  "condition": {
    "expression": {
      "operator": "and",
      "operands": [
        {
          "value": true
        },
        {
          "expression": {
            "operator": "and",
            "operands": [
              {
                "value": true
              },
              {
                "expression": {
                  "operator": "eq",
                  "operands": [
                    {
                      "variable": "R.attr.department"
                    },
                    {
                      "value": "marketing"
                    }
                  ]
                }
              }
            ]
          }
        }
      ]
    }
  }
}
    """

    pf = Parse(data, engine_pb2.PlanResourcesFilter())
    assert pf.kind == engine_pb2.PlanResourcesFilter.KIND_CONDITIONAL

    expr1: engine_pb2.PlanResourcesFilter.Expression.Operand = pf.condition
    assert isinstance(expr1, engine_pb2.PlanResourcesFilter.Expression.Operand)
    assert expr1.expression.operator == "and"
    assert len(expr1.expression.operands) == 2

    value1 = expr1.expression.operands[0]
    assert isinstance(value1, engine_pb2.PlanResourcesFilter.Expression.Operand)
    assert value1.value.HasField("bool_value")
    assert value1.value.bool_value == True

    expr2 = expr1.expression.operands[1]
    assert isinstance(expr2, engine_pb2.PlanResourcesFilter.Expression.Operand)
    assert expr2.expression.operator == "and"
    assert len(expr2.expression.operands) == 2

    value2 = expr2.expression.operands[0]
    assert isinstance(value2, engine_pb2.PlanResourcesFilter.Expression.Operand)
    assert value2.value.HasField("bool_value")
    assert value2.value.bool_value == True

    expr3 = expr2.expression.operands[1]
    assert isinstance(expr3, engine_pb2.PlanResourcesFilter.Expression.Operand)
    assert expr3.expression.operator == "eq"
    assert len(expr3.expression.operands) == 2

    var1 = expr3.expression.operands[0]
    assert isinstance(var1, engine_pb2.PlanResourcesFilter.Expression.Operand)
    assert var1.variable == "R.attr.department"

    value3 = expr3.expression.operands[1]
    assert isinstance(value3, engine_pb2.PlanResourcesFilter.Expression.Operand)
    assert value3.value.HasField("string_value")
    assert value3.value.string_value == "marketing"