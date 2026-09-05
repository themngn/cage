Name:           {{{ git_dir_name }}}
# Hardcoded rather than {{{ git_dir_version }}}: this branch forked before
# the v0.3.1 tag was cut, so git describe resolves against v0.3.0 instead
# (not an ancestor of v0.3.1), giving an auto-derived version like
# "0.0.git.390.<sha>" — which sorts BELOW stock Fedora's cage-0.3.1-1, so
# `dnf install cage` would never actually prefer this COPR build over an
# already-installed stock one. Pin to the upstream version this is based
# on, with a .sichos release suffix, so it always sorts higher.
Version:        0.3.1
Release:        2.sichos%{?dist}
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
