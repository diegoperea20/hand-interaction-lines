import cv2
import mediapipe as mp

# Inicializar el detector de manos de mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configurar la cámara
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Coordenadas del rectángulo
rect_x = width // 3
rect_y = height // 3
rect_width = width // 3
rect_height = height // 3

# Color inicial del rectángulo (rojo)
rect_color = (0, 0, 255)

# Inicializar el estado del rectángulo
rectangle_touched = False

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Voltear la imagen horizontalmente para que coincida con el movimiento de la mano
        frame = cv2.flip(frame, 1)

        # Detección de manos
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dibujar los puntos clave de la mano
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * width), int(landmark.y * height)
                    if rect_x < x < rect_x + rect_width and rect_y < y < rect_y + rect_height:
                        rect_color = (0, 255, 255)  # Cambiar color a amarillo
                        rectangle_touched = True
                        #print("amarillo")

        # Dibujar el rectángulo
        cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), rect_color, -1)

        cv2.imshow('Hand Rectangle Interaction', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
