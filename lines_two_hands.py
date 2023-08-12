import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

line_x = width // 3
line_y_top = height // 3
line_y_bottom = height * 2 // 3
line_height = height // 3

line_color_left = (0, 0, 255)
line_color_right = (0, 0, 255)

left_line_touched = [False, False]
right_line_touched = [False, False]

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        left_line_touched = [False, False]
        right_line_touched = [False, False]

        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * width), int(landmark.y * height)
                    
                    # Tocar la línea izquierda
                    if idx == 0 and line_x - 20 < x < line_x + 20 and line_y_top < y < line_y_bottom:
                        line_color_left = (0, 255, 0)  # Cambiar color a verde
                        left_line_touched[0] = True
                    elif idx == 1 and line_x - 20 < x < line_x + 20 and line_y_top < y < line_y_bottom:
                        line_color_left = (0, 255, 0)  # Cambiar color a verde
                        left_line_touched[1] = True

                    # Tocar la línea derecha
                    if idx == 0 and width - line_x - 20 < x < width - line_x + 20 and line_y_top < y < line_y_bottom:
                        line_color_right = (0, 255, 0)  # Cambiar color a verde
                        right_line_touched[0] = True
                    elif idx == 1 and width - line_x - 20 < x < width - line_x + 20 and line_y_top < y < line_y_bottom:
                        line_color_right = (0, 255, 0)  # Cambiar color a verde
                        right_line_touched[1] = True

        cv2.line(frame, (line_x, line_y_top), (line_x, line_y_bottom), line_color_left if any(left_line_touched) else (0, 0, 255), 10)
        cv2.line(frame, (width - line_x, line_y_top), (width - line_x, line_y_bottom), line_color_right if any(right_line_touched) else (0, 0, 255), 10)

        cv2.imshow('Hand Lines Interaction', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
