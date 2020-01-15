lap_score = 0

function lap_score_with_checkpoints()
  lap_score = data.P1LapCheckpoint + (correct_lap() * 100)
  return lap_score
end

function correct_lap ()
  if data.P1Lap == 127 then
    return 0
  else
    return data.P1Lap + 1
  end
end

