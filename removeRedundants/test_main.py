from main import *


def test_remove_redundants(capsys):
  setOfTrees = createInputSetOfTrees()
  goldenMatrix = createInputGoldenMatrix()
  existingConnections = removeRedundantConnections(setOfTrees, goldenMatrix)
  compareConnections(existingConnections, goldenMatrix)
  captured = capsys.readouterr()
  assert "SUCCESS" in captured.out
