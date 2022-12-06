user { 'fred':
  ensure => present,
  groups => ['my_group']
}
user { 'seth':
  ensure => present,
  groups => ['my_group']
}
group { 'my_group':
  ensure =>present
}
package { 'python':
  ensure => installed,
  provider => pip3
}

$users = [ 'user1', 'user2']

user { $users:
  ensure  => present,
  groups  => ['my_group']
}

package {'pip3':
  require  => Package['python3-pip'],
  ensure   => latest,
  provider => 'pip3'
}

package { ['python3-pip']:
  ensure => installed
}

package { libapache2-mod-wsgi-py3:
  ensure  => installed
}

package { bottle:
  ensure   => '0.10.11',
  provider => 'pip3',
}
