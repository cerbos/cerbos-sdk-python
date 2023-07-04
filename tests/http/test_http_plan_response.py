# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0


from cerbos.sdk.model import *


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

    pf = PlanResourcesFilter.from_json(data)
    assert pf.kind == PlanResourcesFilterKind.CONDITIONAL

    expr1 = pf.condition
    assert isinstance(expr1, PlanResourcesExpression)
    assert expr1.expression.operator == "and"
    assert len(expr1.expression.operands) == 2

    value1 = expr1.expression.operands[0]
    assert isinstance(value1, PlanResourcesValue)
    assert value1.value == True

    expr2 = expr1.expression.operands[1]
    assert isinstance(expr2, PlanResourcesExpression)
    assert expr2.expression.operator == "and"
    assert len(expr2.expression.operands) == 2

    value2 = expr2.expression.operands[0]
    assert isinstance(value2, PlanResourcesValue)
    assert value2.value == True

    expr3 = expr2.expression.operands[1]
    assert isinstance(expr3, PlanResourcesExpression)
    assert expr3.expression.operator == "eq"
    assert len(expr3.expression.operands) == 2

    var1 = expr3.expression.operands[0]
    assert isinstance(var1, PlanResourcesVariable)
    assert var1.variable == "R.attr.department"

    value3 = expr3.expression.operands[1]
    assert isinstance(value3, PlanResourcesValue)
    assert value3.value == "marketing"
