Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        A Wayland kiosk (SichOS fork — multi-monitor SDDM login fix)

License:        MIT
URL:            https://github.com/themngn/cage
VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)

%description
This is Cage, a Wayland kiosk. A kiosk runs a single, maximized application.

This build carries one fix on top of upstream: xdg_toplevel::set_fullscreen(output)'s
requested output is now actually honored instead of cage always maximizing to the
union of every connected monitor's geometry. Without it, any client that fullscreens
one toplevel per screen on its own output — which is exactly what SDDM's greeter does
per-monitor — gets every one of those toplevels stretched across the combined
resolution of all monitors instead of each appearing correctly on the one it asked
for, so a multi-monitor SDDM login screen ends up stretched across every display
instead of each screen showing its own correctly cropped background.

See https://github.com/themngn/cage/commits/fullscreen-per-output for the fix itself,
and https://github.com/themngn/sichos-lake's CLAUDE.md for the full investigation.

%prep
{{{ git_dir_setup_macro }}}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
{{{ git_dir_changelog }}}
