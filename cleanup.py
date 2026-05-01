import os

DOC_DIR = r"d:\graduation-thesis\document"
IMG_DIR = os.path.join(DOC_DIR, "images")

keep_py = [
    "compile_latex.py",
    "compile_v5.py",
    "config.py",
    "build_all.py",
    "cleanup.py"
]

keep_images = [
    "ai_ml_dl_hierarchy.png",
    "cnn_vi2_1777524446152.png",
    "transfer_learning_vi.png",
    "face_mesh_468.png",
    "triplet_loss_vi.png",
    "hnsw_graph_architecture.png",
    "ear_vi2_1777524475090.png",
    "headpose_vi2_1777524488532.png",
    "wasm_architecture_comparison.png",
    "usecase_diagram.png",
    "activity_diagram.png",
    "hybrid_architecture_diagram_1777606426835.png",
    "pipeline_vi_new.png",
    "face_biometric_auth_1777606446899.png",
    "liveness_vi2_1777524433515.png",
    "sliding_window_diagram.png",
    "erd_diagram.png",
    "placeholder_scenario_focused.png",
    "placeholder_scenario_distracted.png",
    "placeholder_scenario_drowsy.png",
    "placeholder_scenario_identity.png",
    "confusion_matrix_final.png",
    "evaluation_chart.png",
    "placeholder_liveness_test.png"
]

print("--- Deleting unused Python files ---")
for f in os.listdir(DOC_DIR):
    if f.endswith('.py') and f not in keep_py:
        path = os.path.join(DOC_DIR, f)
        os.remove(path)
        print(f"Deleted {f}")

print("\n--- Deleting unused Image files ---")
for f in os.listdir(IMG_DIR):
    if f.endswith('.png') and f not in keep_images and not f.startswith("eq_"):
        path = os.path.join(IMG_DIR, f)
        os.remove(path)
        print(f"Deleted {f}")

print("\nCleanup completed.")
