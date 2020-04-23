
function p1_lap_score_with_checkpoints ()
  local correct_lap = 0
  if data.P1Lap ~= 127 then
    correct_lap = data.P1Lap + 1
  end
  return data.P1LapCheckpoint + (correct_lap * 100)
end

function p2_lap_score_with_checkpoints ()
  local correct_lap = 0
  if data.P2Lap ~= 127 then
    correct_lap = data.P2Lap + 1
  end
  return data.P2LapCheckpoint + (correct_lap * 100)
end
