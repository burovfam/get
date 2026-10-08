import time
def get_triangle_wave_amplitude(freq, t):
    phase = (t * freq) % 1.0
    if phase < 0.5: return phase * 2.0
    else: return (1.0- phase) * 2.0

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1.0 / sampling_frequency)
    