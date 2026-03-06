```bash
cd /home/asecomputerlab/KDeepak/trial4/f3set
# Extract frames

python3 custom_utils/extract_frames_custom.py ../videos/input4.mp4 ../frames/input4

# Create annotation

python3 custom_utils/create_annotation.py input4 ../frames

# Run inference

python3 inference_custom_video.py f3set-model/f3ed ../frames -s test -d custom -o predictions_input4.txt  

# View results

echo -e "\n========== RESULTS ==========\n"

cat predictions_input2.txt
```


**Histogram Output Generation**

```bash
cd /home/asecomputerlab/KDeepak/trial4/f3set

python3 custom_utils/confidence_histogram.py \

--model_dir f3set-model/f3ed \

--frame_dir ../frames \

--split test \

--dataset custom \

--which coarse \

--out hist_input4.png \

--outcsv raw_scores_input4.csv
```

