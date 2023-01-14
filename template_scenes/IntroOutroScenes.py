# Standard libraries
import json
# Third-party libraries
from manim import *
import numpy as np


class IntroScene(Scene):

    def construct(self):
        '''
        Assembles and runs the opening scene. 
        '''
        # import settings and set title y coordinate
        with open('intro_settings.json') as f:
            params = json.load(f)
        up_coord = 4.0
        if params["media"] == "blank":
            up_coord = 1.2

        # init and position MObjects
        # title
        title = Text(params["title"], font_size = 30, font = 'TeX Gyre Schola Math')
        title.next_to(Dot(np.array([0,up_coord,0])), DOWN)
        # headline
        headline = Text(params["headline"], font_size = 25, font = 'TeX Gyre Schola Math')
        headline.next_to(title, DOWN)
        # date
        date = Text(params["date"], font_size = 20, font = 'TeX Gyre Schola Math')
        date.next_to(headline, DOWN)
        # footer image
        footer = ImageMobject(params["footer_file"])
        footer.scale(params["footer_scale"])
        footer.next_to(Dot(np.array([0,-2.5,0])), DOWN)
        
        # add title, headline and date to the opening scene
        self.add(title)
        self.add(headline)
        self.add(date)
        self.wait(params["before_start_wait"])

        # depending on media settings: play custom animation, fade in png
        # or do nothing
        if params["media"] == "custom":
            self.custom_animation(params)
        elif params["media"] == "png":
            self.play_png(params)
        
        if params["media"] != "blank":
            self.wait(params["before_footer_wait"])
        
        # play the footer fade in, wait a bit, then end the video
        self.play(FadeIn(footer))
        self.wait(params["after_footer_wait"])

    def custom_animation(self, params):
        '''
        Provides a custom animation that plays after the title is written. Add your implementation here!
        '''
        # fade in a screen
        image = ImageMobject(params["media_path"])
        image.scale(params["media_scale"])
        image.next_to(Dot(np.array([0,2.3,0])), DOWN)
        self.play(FadeIn(image)) 
        # start typing...
        fft_string = """
        void fft(Iter\_T a, Iter\_T b, int log2n)
        {
        typedef typename iterator\_traits<Iter\_T>::value\_type complex;
        const complex J(0, 1);
        int n = 1 << log2n;
        for (unsigned int i=0; i < n; ++i) {
            b[bitReverse(i, log2n)] = a[i];
        }
        for (int s = 1; s <= log2n; ++s) {
            int m = 1 << s;
            int m2 = m >> 1;
            complex w(1, 0);
            complex wm = exp(-J * (PI / m2));
            for (int j=0; j < m2; ++j) {
            for (int k=j; k < n; k += m) {
                complex t = w * b[k + m2];
                complex u = b[k];
                b[k] = u + t;
                b[k + m2] = u - t;
            }
            w *= wm;
            }
        }
        }
        """
        text = MarkupText('<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')
        fft_code = Text(fft_string, font_size = 5.5, font = "Ubuntu Mono")
        text.next_to(Dot(np.array([-1.45,1.3,0])), DOWN)
        self.play(Write(fft_code))

    def play_png(self, params):
        '''
        Fades in a .png file given in params["media_path"] at the center of the scene
        '''
        image = ImageMobject(params["media_path"])
        image.scale(params["media_scale"])
        image.next_to(Dot(np.array([0,1.8,0])), DOWN)
        self.play(FadeIn(image))    
