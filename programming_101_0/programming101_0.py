# Standard libraries
import json
import os
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

        # fade out with the titles
        fade_out_group = [
            FadeOut(title),
            FadeOut(headline),
            FadeOut(date),
            FadeOut(footer)
        ]
        self.play(*fade_out_group, lag_ratio = 0.0)

        scale = 3.0
        matrix_scale = [[scale,0],[0,scale]]
        self.play(ApplyMatrix(matrix_scale, self.fft_code), ApplyMatrix(matrix_scale, self.screen_image))

        # Draw a rectangle for the movie scenes 
        self.rect = Rectangle(width=12.5, height=7)
        self.rect.next_to(Dot(np.array([0,4.0, 0])), DOWN)
        self.play(FadeOut(self.screen_image), Create(self.rect))
        self.wait(0.5)
        self.play(FadeOut(self.fft_code))

        # List the names of movies underneath
        section_from = "Részlet a {movie_title} c. {media_type} ({movie_date})"
        type_list = ["filmből", "filmből", "filmből", "sorozatból"]
        movie_list = ["Mátrix", "Komputerkémek", "Vasember", "Mr. Robot"]
        movie_dates = ["1999", "1981", "2004", "2014"]
        first = True
        self.movie_cite = Text(section_from.format(
                movie_title = movie_list[0],
                movie_date = movie_dates[0],
                media_type = type_list[0]),
            font_size = 20, font = "Ubuntu Mono")
        
        movie_text_height = -3.2

        self.movie_cite.next_to(Dot(np.array([0,movie_text_height,0])), DOWN)
        for title, date, media_type in zip(movie_list, movie_dates, type_list):
            # add the title of the movies with their dates 
            if first:
                first = False
                self.play(Write(self.movie_cite))
                self.wait(2)
            else:
                self.new_movie_cite = Text(section_from.format(
                        movie_title = title, 
                        movie_date = date,
                        media_type = media_type),
                    font_size = 20, font = "Ubuntu Mono")
                self.new_movie_cite.next_to(Dot(np.array([0,movie_text_height,0])), DOWN)
                self.play(ReplacementTransform(self.movie_cite, self.new_movie_cite))
                self.movie_cite = self.new_movie_cite
                self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # display some of the courses you can sign up to
        0
        
        self.chapter_title = Text("Elérhető kurzusok...", font_size = 30, font = "Ubuntu Mono")
        self.chapter_title.next_to(Dot(np.array([0,up_coord,0])), DOWN)
        
        self.current_components = []
        self.highlight_boxes = []
        
        course_types = ["universities", "free_courses", "paid_courses"]
        course_texts = ["Egyetemek", "Ingyen kurzusok", "Fizetős kurzusok"]
        
        for course_type, course_text in zip(course_types,course_texts):
            # write text
            sub = Text(course_text,
                font_size = 20,
                font = "Ubuntu Mono")
            self.current_components.append(sub)
            highlight_box = Rectangle(width = sub.width + 0.1, height = sub.height+0.2)
            self.highlight_boxes.append(highlight_box)
            
            for media_name in params[course_type]:
                media_path = os.path.join(params["logo_path"], media_name)
                image = ImageMobject(media_path)
                image.scale_to_fit_height(1.2)
                if media_name == ["bme.png"] or media_name == ["coursera.png"]:
                    image.scale_to_fit_height(0.4)
                self.current_components.append(image)
        
        self.current_group = Group(*self.current_components)
        self.current_group.arrange_in_grid(rows = 3, buff = 0.5)
        for idx, box in enumerate(self.highlight_boxes):
            center = self.current_components[4*idx].get_center()
            box.move_to([center[0], center[1], 0.0])
        self.play(Write(self.chapter_title))
        self.play(FadeIn(self.current_group))
        self.wait(2)
        self.play(Create(self.highlight_boxes[0]))
        self.wait(2)
        # try modifying the course icons for display
        self.play(self.current_components[5].animate.scale(1.7))
        self.wait(3)
        self.play(self.current_components[5].animate.scale(1/1.7))
        self.wait(3)
        self.play(self.current_components[7].animate.scale(1.7))
        self.wait(3)
        self.play(self.current_components[7].animate.scale(1/1.7))
        self.wait(3)
        # scroll thru highlight boxes
        for idx in range(len(self.highlight_boxes)-1):
            self.play(ReplacementTransform(self.highlight_boxes[idx],
                self.highlight_boxes[idx+1]))
            self.wait(3)
        # move a rectangle along the different types
        # Wiki lookup
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wiki_attributes = []
        self.wiki_logo = ImageMobject(os.path.join(params["logo_path"], "wiki_logo.png"))
        self.wiki_logo.scale_to_fit_height(6)
        self.wiki_attributes.append(self.wiki_logo)
        self.play(FadeIn(self.wiki_logo))
        self.wait(2)
        self.play(self.wiki_logo.animate.scale(0.25), duration = 0.4)
        self.play(self.wiki_logo.animate.move_to([-6.0, 2.6, 0.0]))
        self.prog_def = Text(params["programming_def_wiki"],
            font_size = 20, font = "Ubuntu Mono")
        self.prog_def.next_to(Dot(np.array([1.0, 3.5, 0.0])), DOWN)
        self.wiki_attributes.append(self.prog_def)
        self.play(Write(self.prog_def))
        self.wait(3)
        
        self.algo_def = Text(params["algo_def"],
            font_size = 17, font = "Ubuntu Mono")
        self.language_def = Text(params["language_def"],
            font_size = 17, font = "Ubuntu Mono")

        self.algo_def.next_to(Dot(np.array([-3.5,1.5,0.0])), DOWN)
        self.wiki_attributes.append(self.algo_def)
        self.language_def.next_to(Dot(np.array([3.5,1.5,0.0])), DOWN)
        self.wiki_attributes.append(self.language_def)
        self.play(Write(self.algo_def), Write(self.language_def))
        self.wait(2)

        box_no = 3
        flowchart = []
        box_w = 1.0
        box_h = 2.0
        for box_idx in range(box_no):
            current_box = Rectangle(width = 3.85, height = 1.2)
            flowchart.append(current_box)
            if box_idx < box_no - 1:
                current_arrow = Arrow(start=LEFT, end=RIGHT, color = BLUE, max_stroke_width_to_length_ratio=2.5)
                current_arrow = VMobject.scale(current_arrow,0.5)
                flowchart.append(current_arrow)
        # distribute 
        
        self.algo_visualization = VGroup(*flowchart)
        self.algo_visualization.arrange_in_grid(rows = 1, buff = 0.1)
        self.algo_visualization.next_to(Dot(np.array([0.0,0.5, 0.0])),DOWN)

        svg_algo_path = params["svg_algo_path"]
        svg_files = params["svg_algo_files"]        
        svg_objects = [SVGMobject(file_name = os.path.join(svg_algo_path, svg_files[i]), color = WHITE) for i in range(len(svg_files))]
        current_icon = svg_objects[0]
        current_icon.next_to(self.algo_visualization, DOWN)
        self.play(FadeIn(current_icon))
        self.wait(3)
        
        
        self.play(FadeIn(self.algo_visualization), duration = 0.5)
        self.wait(3)
        # switching captions

        
        text_list = []
        cap_size = 17
        for box_idx in range(box_no):
            current_box = flowchart[2*box_idx]
            center = current_box.get_center()
            caption = Text(params["algo_captions"][0][box_idx], font_size = cap_size, font = "Ubuntu Mono")
            caption.move_to([center[0], center[1], 0.0])
            text_list.append(caption)
            self.play(Write(caption))
        
        
        num_of_switches = len(svg_files) - 1
        # iterate thru texts and transform
        for switch_idx in range(num_of_switches):
            new_icon = svg_objects[switch_idx + 1]
            new_icon.next_to(self.algo_visualization, DOWN)
            self.play(ReplacementTransform(current_icon, new_icon))
            current_icon = new_icon
            for box_idx in range(box_no):
                # transform box contents
                current_box = flowchart[2*box_idx]
                caption = Text(params["algo_captions"][switch_idx + 1][box_idx], font_size = cap_size, font = "Ubuntu Mono")
                center = current_box.get_center()
                caption.move_to([center[0], center[1], 0.0])
                self.play(ReplacementTransform(text_list[box_idx], caption))
                text_list[box_idx] = caption
            
            self.wait(5)
        
        # Move this to the side
        self.full_algo_visualization = [self.algo_visualization] + text_list + [current_icon]
        self.full_algo_visualization_group = Group(*self.full_algo_visualization)
        self.wiki_attributes = self.wiki_attributes + self.full_algo_visualization
        self.play(self.full_algo_visualization_group.animate.scale(0.5), duration = 0.4)
        self.play(self.full_algo_visualization_group.animate.move_to([-3.5, -1.5, 0.0]))
        
        self.wait(3)
        
        # Computer with a speech bubble, w. some languages
        self.screen_image.scale(0.125)
        #self.screen_image.next_to(Dot(np.array([3,0.0,0])), DOWN)
         
        # Add bubble
        self.speech_bubble = SVGMobject(file_name = os.path.join(svg_algo_path, params['bubble_path']), color = WHITE, stroke_width=0.1)
        self.speech_bubble.next_to(Dot(np.array([1.5,1.5,0])), DOWN)
        self.speech_bubble.scale(0.85)
        
        

        self.prog_languages = Text(params["prog_languages"], font_size = 15, font = "Ubuntu Mono")
        self.prog_languages.next_to(Dot(np.array([0.5,0.33,0]), DOWN))
        
        self.prog_languages_group = Group(self.screen_image, self.speech_bubble, self.prog_languages)
        self.prog_languages_group.next_to(Dot(np.array([3.0,0.8,0.0])), DOWN)

        self.wait(5)
        self.play(FadeIn(self.screen_image), FadeIn(self.speech_bubble))
        self.play(Write(self.prog_languages))
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.wiki_attributes]
        )
        self.play(self.prog_languages_group.animate.move_to([3.5, 0.0, 0.0]))
        self.play(self.prog_languages_group.animate.scale(1.25))
        self.wait(5)
        # load wiki, youtube logo, then fortnite/insta/tiktok...

        # erase all exept screen_im and prog languages
        # Sequence of instructions - the trivial applications:
        # Sec. school kids: wiki logo, youtube logo, fortnite... even making this video!
        # How much software runs on PC/phone compared to others?
        # Iceberg!
        # What could hackers stop in Ukraine?
        # All right, how many devs are out there... and if I'm not one?
        # Stipi scholars
        # Notes on the course itself 


    def custom_animation(self, params):
        '''
        Provides a custom animation that plays after the title is written. Add your implementation here!
        '''
        # fade in a screen
        self.screen_image = ImageMobject(params["media_path"])
        self.screen_image.scale(params["media_scale"])
        self.screen_image.next_to(Dot(np.array([0,2.3,0])), DOWN)
        self.play(FadeIn(self.screen_image)) 
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
        self.fft_code = Text(fft_string, font_size = 6, font = "Ubuntu Mono")
        self.fft_code.next_to(Dot(np.array([-0.4,1.4,0])), DOWN)
        self.play(Write(self.fft_code))


    def play_png(self, params):
        '''
        Fades in a .png file given in params["media_path"] at the center of the scene
        '''
        image = ImageMobject(params["media_path"])
        image.scale(params["media_scale"])
        image.next_to(Dot(np.array([0,1.8,0])), DOWN)
        self.play(FadeIn(image))    
